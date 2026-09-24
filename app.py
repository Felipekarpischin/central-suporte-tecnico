"""API REST local de Service Desk para portfólio."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import sqlite3
from urllib.parse import parse_qs, urlparse

DB_PATH = "tickets.db"
PRIORITIES = {"low", "medium", "high", "critical"}
STATUSES = {"open", "in_progress", "resolved", "closed"}

def connect_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with connect_db() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open',
                assignee TEXT
            )
        """)

def as_dict(row):
    return dict(row)

class ServiceDeskHandler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        raw = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(raw)

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length) or b"{}")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PATCH, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        route = urlparse(self.path)
        query = parse_qs(route.query)
        if route.path == "/health":
            return self.send_json(200, {"status": "ok", "service": "central-suporte-tecnico"})
        if route.path == "/metrics":
            with connect_db() as connection:
                total = connection.execute("SELECT COUNT(*) FROM tickets").fetchone()[0]
                open_count = connection.execute("SELECT COUNT(*) FROM tickets WHERE status = 'open'").fetchone()[0]
                by_priority = {p: connection.execute("SELECT COUNT(*) FROM tickets WHERE priority = ?", (p,)).fetchone()[0] for p in sorted(PRIORITIES)}
            return self.send_json(200, {"total": total, "open": open_count, "by_priority": by_priority})
        if route.path == "/tickets":
            filters = []
            values = []
            for field in ("status", "priority"):
                value = query.get(field, [None])[0]
                if value:
                    if value not in (STATUSES if field == "status" else PRIORITIES):
                        return self.send_json(400, {"error": f"{field} inválido"})
                    filters.append(f"{field} = ?")
                    values.append(value)
            sql = "SELECT * FROM tickets" + ((" WHERE " + " AND ".join(filters)) if filters else "") + " ORDER BY id DESC"
            with connect_db() as connection:
                rows = connection.execute(sql, values).fetchall()
            return self.send_json(200, [as_dict(row) for row in rows])
        return self.send_json(404, {"error": "rota não encontrada"})

    def do_POST(self):
        if urlparse(self.path).path != "/tickets":
            return self.send_json(404, {"error": "rota não encontrada"})
        try:
            data = self.read_json()
        except (json.JSONDecodeError, UnicodeDecodeError):
            return self.send_json(400, {"error": "JSON inválido"})
        required = ("requester", "category", "description")
        if not all(str(data.get(key, "")).strip() for key in required):
            return self.send_json(400, {"error": "campos obrigatórios ausentes"})
        priority = data.get("priority", "medium")
        if priority not in PRIORITIES:
            return self.send_json(400, {"error": "prioridade inválida"})
        values = tuple(str(data[key]).strip() for key in required) + (priority,)
        with connect_db() as connection:
            cursor = connection.execute("INSERT INTO tickets (requester, category, description, priority) VALUES (?, ?, ?, ?)", values)
            row = connection.execute("SELECT * FROM tickets WHERE id = ?", (cursor.lastrowid,)).fetchone()
        return self.send_json(201, as_dict(row))

    def do_PATCH(self):
        parts = urlparse(self.path).path.rstrip("/").split("/")
        if len(parts) != 2 or parts[0] != "/tickets" or not parts[1].isdigit():
            return self.send_json(404, {"error": "rota não encontrada"})
        try:
            data = self.read_json()
        except (json.JSONDecodeError, UnicodeDecodeError):
            return self.send_json(400, {"error": "JSON inválido"})
        if "status" in data and data["status"] not in STATUSES:
            return self.send_json(400, {"error": "status inválido"})
        changes = []
        values = []
        for field in ("status", "assignee"):
            if field in data:
                changes.append(f"{field} = ?")
                values.append(str(data[field]).strip() or None)
        if not changes:
            return self.send_json(400, {"error": "nenhuma alteração informada"})
        values.append(int(parts[1]))
        with connect_db() as connection:
            cursor = connection.execute(f"UPDATE tickets SET {', '.join(changes)} WHERE id = ?", values)
            if cursor.rowcount == 0:
                return self.send_json(404, {"error": "chamado não encontrado"})
            row = connection.execute("SELECT * FROM tickets WHERE id = ?", (int(parts[1]),)).fetchone()
        return self.send_json(200, as_dict(row))

if __name__ == "__main__":
    init_db()
    print("Support Desk API: http://localhost:8000")
    ThreadingHTTPServer(("localhost", 8000), ServiceDeskHandler).serve_forever()
 

# Alias mantido para compatibilidade com testes e integrações existentes.
handler = ServiceDeskHandler
