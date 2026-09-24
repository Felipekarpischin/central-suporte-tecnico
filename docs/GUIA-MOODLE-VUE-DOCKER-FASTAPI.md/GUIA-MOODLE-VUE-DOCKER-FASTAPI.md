# Apostila prática: Moodle, Vue, Docker e FastAPI

Guia introdutório criado para estudo e portfólio. Os exemplos são didáticos e não substituem experiência profissional real.

## Como usar este guia

1. Leia o conceito.
2. Execute o exemplo em ambiente local.
3. Registre o que você conseguiu reproduzir.
4. Só informe no currículo aquilo que consegue explicar em entrevista.

## 1. Moodle: suporte e operação

Moodle é uma plataforma de gestão da aprendizagem (LMS). Em uma equipe de suporte, o trabalho normalmente envolve usuários, cursos, permissões, atividades, relatórios e diagnóstico de problemas.

### Fluxo básico de atendimento

- Confirmar usuário, curso, turma e navegador.
- Reproduzir o problema sem alterar dados reais.
- Verificar permissões, matrícula, atividade e prazo.
- Registrar evidências, horário e mensagem de erro.
- Orientar o usuário com passos claros.
- Encerrar somente após validar a solução.

### O que estudar

- Papéis: administrador, professor, estudante e gerente.
- Cursos, categorias, matrícula e conclusão.
- Atividades, notas, fóruns e arquivos.
- Backup, restauração e atualização controlada.
- Privacidade, menor privilégio e registro de chamados.

### Projeto de portfólio recomendado

Criar um manual de suporte para um Moodle fictício: catálogo de incidentes, checklist de diagnóstico, respostas ao usuário e matriz de escalonamento. Isso demonstra raciocínio de suporte EaD, mas não deve ser descrito como administração de Moodle em produção.

## 2. Vue: interface reativa

Vue é um framework JavaScript para construir interfaces baseadas em componentes e estado reativo.

### Exemplo mínimo

```html
<div id="app">
  <input v-model="filtro" placeholder="Filtrar">
  <p v-for="chamado in filtrados" :key="chamado.id">
    {{ chamado.titulo }} - {{ chamado.status }}
  </p>
</div>
<script>
const { createApp, computed, ref } = Vue;
createApp({
  setup() {
    const filtro = ref('');
    const chamados = ref([{ id: 1, titulo: 'Acesso', status: 'Aberto' }]);
    const filtrados = computed(() => chamados.value.filter(c => c.titulo.toLowerCase().includes(filtro.value.toLowerCase())));
    return { filtro, filtrados };
  }
}).mount('#app');
</script>
```

Conceitos importantes: componentes, props, eventos, estado reativo, computed, ciclo de vida e consumo de API.

## 3. Docker: ambientes reproduzíveis

Docker empacota uma aplicação e suas dependências em uma imagem executável. Isso reduz diferenças entre máquinas e facilita testes.

### Dockerfile didático para uma API Python

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

Comandos essenciais:

```bash
docker build -t central-suporte .
docker run --rm -p 8000:8000 central-suporte
```

Boas práticas: imagem pequena, nenhuma senha na imagem, usuário sem privilégio quando possível, volumes para dados persistentes e tags versionadas.

## 4. FastAPI: API moderna em Python

FastAPI é um framework Python para APIs com validação por tipos e documentação automática.

### Exemplo mínimo

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Central de Suporte")

class Ticket(BaseModel):
    requester: str
    description: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    return {"id": 1, **ticket.model_dump()}
```

Execução local:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

A documentação fica em /docs. Em um projeto real, acrescente autenticação, banco, logs, testes e controle de CORS.

## Projeto integrado sugerido

Evoluir a Central de Suporte Técnico com uma interface Vue, uma API FastAPI, banco SQLite/PostgreSQL e Docker. O Moodle entra como cenário de negócio: chamados sobre matrícula, acesso, atividades e arquivos.

Entregáveis recomendados:

- README com arquitetura e decisões.
- API com /health, /tickets e /metrics.
- Interface com criação e filtros.
- Testes de validação.
- Dockerfile reproduzível.
- Manual de suporte Moodle fictício.

## Como declarar corretamente no currículo

Use: Conhecimentos em estudo e projeto de portfólio envolvendo suporte a fluxos EaD/Moodle, interfaces web, APIs Python e containerização Docker.

Não use: experiência profissional com Moodle, Vue, Docker ou FastAPI, caso essa experiência ainda não tenha ocorrido em empresa ou projeto real comprovável.

## Checklist de entrevista

- Explique o fluxo de uma requisição HTTP.
- Diferencie imagem e container.
- Explique estado reativo no Vue.
- Mostre como validaria um chamado.
- Descreva como investigaria um problema de acesso no Moodle.
- Cite limitações e próximos passos do projeto.
