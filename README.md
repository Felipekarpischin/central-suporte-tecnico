# Central de Suporte Técnico

Projeto de portfólio para demonstrar uma API REST em Python voltada à organização, triagem e acompanhamento de chamados de Service Desk.

Projeto prático de portfólio, sem representar experiência profissional em empresa.

## Funcionalidades

- Criar chamados com solicitante, categoria, descrição e prioridade.
- Persistir dados localmente em SQLite.
- Atualizar status e responsável pelo atendimento.
- Filtrar chamados por status e prioridade.
- Exibir métricas operacionais básicas.
- Validar dados de entrada e responder em JSON.
- Endpoint de saúde para verificação do serviço.

## Tecnologias

Python 3.11+, biblioteca padrão, HTTP REST, JSON, SQLite, dataclasses e unittest.

## Endpoints

- GET /health: verifica se o serviço está ativo.
- GET /tickets: lista chamados; aceita filtros status e priority.
- POST /tickets: cria um chamado.
- PATCH /tickets/{id}: atualiza status ou responsável.
- GET /metrics: retorna total, chamados abertos e distribuição por prioridade.

## Execução

```bash
python app.py
```

A API estará em http://localhost:8000 e criará o arquivo local tickets.db automaticamente.

## Exemplos

```bash
curl http://localhost:8000/health
curl http://localhost:8000/tickets
curl http://localhost:8000/metrics
```

Para criar um chamado:

```bash
curl -X POST http://localhost:8000/tickets -H "Content-Type: application/json" -d "{\"requester\":\"Ana\",\"category\":\"Acesso\",\"description\":\"Não consigo acessar o sistema\",\"priority\":\"high\"}"
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Qualidade e segurança

- Consultas ao SQLite usam parâmetros, evitando SQL construído com dados de entrada.
- Validação de campos obrigatórios, prioridade e status.
- Respostas JSON padronizadas.
- Não contém credenciais nem dados pessoais reais.
- Execução local e reprodução simples.

## Limitações

O projeto ainda não possui autenticação, interface web, implantação pública ou documentação OpenAPI. Essas limitações estão registradas para diferenciar funcionalidades implementadas de melhorias futuras.

## Próximas melhorias

- Autenticação e autorização.
- Interface web responsiva.
- OpenAPI/Swagger.
- Docker.
- Indicadores de SLA.
- Implantação em ambiente de demonstração.

## Como apresentar no currículo

Projeto de portfólio: desenvolvimento de API REST em Python para registro, triagem e acompanhamento de chamados de Service Desk, com persistência SQLite, validação, filtros, métricas, testes automatizados e documentação técnica.

## Autor

Felipe Karpischin Pinto

GitHub: https://github.com/Felipekarpischin
Projeto: https://github.com/Felipekarpischin/central-suporte-tecnico

## Interface web demonstrável

A pasta web/ contém uma interface responsiva e funcional para demonstrar abertura e consulta de chamados no navegador. Ela utiliza localStorage somente no modo demonstração, sem alegar persistência em produção.

Abra web/index.html para testar o painel, registrar chamados e filtrar por status.

## Portfólio complementar

- GitHub e projeto funcional: https://github.com/Felipekarpischin/central-suporte-tecnico
- Guia técnico: https://github.com/Felipekarpischin/central-suporte-tecnico/blob/main/docs/GUIA-MOODLE-VUE-DOCKER-FASTAPI.md
- Blog editorial Game Vault 47: https://gamevault47.blogspot.com/

O Blogger demonstra produção de conteúdo, documentação e comunicação escrita. O blog é focado em games e, por isso, é apresentado como portfólio complementar, não como experiência profissional de desenvolvimento web, Moodle ou suporte EaD.
