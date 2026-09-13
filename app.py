"""API local de Service Desk para portfólio."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from urllib.parse import urlparse, parse_qs
tickets=[]
next_id=1
PRIORITIES={"low","medium","high","critical"}
STATUSES={"open","in_progress","resolved","closed"}
def payload():
    length=int(handler.headers.get("Content-Length",0))
    return json.loads(handler.rfile.read(length) or b"{}")
class handler(BaseHTTPRequestHandler):
    def send_json(self,status,data):
        raw=json.dumps(data,ensure_ascii=False).encode(); self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        route=urlparse(self.path); q=parse_qs(route.query)
        if route.path=="/metrics": return self.send_json(200,{"total":len(tickets),"open":sum(t["status"]=="open" for t in tickets),"by_priority":{p:sum(t["priority"]==p for t in tickets) for p in sorted(PRIORITIES)}})
        if route.path=="/tickets": return self.send_json(200,[t for t in tickets if (not q.get("status") or t["status"]==q["status"][0]) and (not q.get("priority") or t["priority"]==q["priority"][0])])
        self.send_json(404,{"error":"rota não encontrada"})
    def do_POST(self):
        global next_id
        if self.path!="/tickets": return self.send_json(404,{"error":"rota não encontrada"})
        try: data=payload()
        except json.JSONDecodeError: return self.send_json(400,{"error":"JSON inválido"})
        if not all(str(data.get(k," ")).strip() for k in ("requester","category","description")): return self.send_json(400,{"error":"campos obrigatórios ausentes"})
        if data.get("priority","medium") not in PRIORITIES: return self.send_json(400,{"error":"prioridade inválida"})
        ticket={"id":next_id,"requester":data["requester"].strip(),"category":data["category"].strip(),"description":data["description"].strip(),"priority":data.get("priority","medium"),"status":"open","assignee":None}; tickets.append(ticket); next_id+=1; return self.send_json(201,ticket)
    def do_PATCH(self):
        if not self.path.startswith("/tickets/"): return self.send_json(404,{"error":"rota não encontrada"})
        try: data=payload(); ticket=next(t for t in tickets if t["id"]==int(self.path.rsplit("/",1)[1]))
        except (ValueError,KeyError,StopIteration,json.JSONDecodeError): return self.send_json(404,{"error":"chamado não encontrado"})
        if "status" in data and data["status"] not in STATUSES: return self.send_json(400,{"error":"status inválido"})
        if "status" in data: ticket["status"]=data["status"]
        if "assignee" in data: ticket["assignee"]=str(data["assignee"]).strip() or None
        return self.send_json(200,ticket)
if __name__=="__main__":
    print("Support Desk API: http://localhost:8000")
    ThreadingHTTPServer(("localhost",8000),handler).serve_forever()
