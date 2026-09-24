# Central de Suporte Técnico

Projeto de portfólio desenvolvido para demonstrar uma API REST em Python voltada à organização, triagem e acompanhamento de chamados de Service Desk.

> Projeto prático de portfólio. Não representa experiência profissional em empresa.

## Objetivo

Simular uma central de atendimento técnico com foco em registro de solicitações, priorização, atualização de status e acompanhamento de indicadores operacionais.

## Funcionalidades

- Criar chamados com solicitante, categoria, descrição e prioridade.
- Atualizar status e responsável pelo atendimento.
- Filtrar chamados por status e prioridade.
- Exibir indicadores operacionais básicos.
- Validar dados de entrada e responder em JSON.
- Organizar o código em uma estrutura simples, legível e reproduzível.

## Tecnologias e conceitos demonstrados

- Python 3.11+
- API REST e comunicação HTTP
- JSON
- Modelagem com dataclasses
- Validação de dados
- Testes automatizados com unittest
- Organização de chamados e lógica de Service Desk
- Documentação técnica e instruções de execução

## Estrutura do projeto

- app.py: implementação da API e regras principais.
- tests/: testes automatizados.
- README.md: documentação, execução e apresentação do projeto.

## Execução local

```bash
python app.py
```

A API ficará disponível em:

http://localhost:8000

## Testes

```bash
python -m unittest discover -s tests -v
```

## Exemplos de uso

A API pode ser utilizada para criar, consultar, filtrar e atualizar chamados, permitindo demonstrar um fluxo básico de atendimento técnico.

Para explorar os endpoints, execute a aplicação localmente e utilize um navegador, cURL, Postman ou outra ferramenta compatível com HTTP.

## Qualidade e segurança

- Validação de dados antes do processamento.
- Respostas estruturadas em JSON.
- Projeto sem credenciais ou dados pessoais reais.
- Execução local para facilitar testes e reprodução.
- Escopo reduzido para manter o código compreensível e auditável.

## Limitações atuais

Este projeto não utiliza banco de dados persistente, autenticação de usuários ou implantação em produção. Essas limitações são intencionais nesta versão de portfólio e estão registradas para orientar a evolução futura.

## Próximas melhorias

- Persistência com SQLite ou PostgreSQL.
- Autenticação e autorização de usuários.
- Documentação OpenAPI/Swagger.
- Containerização com Docker.
- Interface web responsiva.
- Integração com indicadores de SLA.
- Implantação em ambiente de demonstração.

## Relação com minha formação

O projeto conecta conhecimentos de Análise e Desenvolvimento de Sistemas, programação, APIs, bancos de dados, testes e suporte técnico. Também demonstra capacidade de documentar uma solução e explicar suas decisões técnicas.

## Como apresentar no currículo

**Projeto de portfólio — Central de Suporte Técnico:** desenvolvimento de API REST em Python para registro, triagem e acompanhamento de chamados de Service Desk, com validação, filtros, indicadores operacionais, testes automatizados e documentação técnica.

## Autor

Felipe Karpischin Pinto

- GitHub: https://github.com/Felipekarpischin
- Projeto: https://github.com/Felipekarpischin/central-suporte-tecnico
