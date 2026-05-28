# Mini Flask API

Projeto simples em Flask para demonstrar:

- APIs REST
- testes unitários
- testes funcionais
- cache com Redis
- persistência com TinyDB
- coverage
- SonarQube

## Instalação

```bash
pip install -r requirements.txt
````

## Executando

```bash
python3 app.py
```

API disponível em:

```text
http://127.0.0.1:5000
```

---

## Endpoints

### Soma

```bash
curl -X POST \
http://127.0.0.1:5000/sum \
-H "Content-Type: application/json" \
-d '{"a":10,"b":5}'
```

### Computar $\pi$

```bash
curl -X POST \
http://127.0.0.1:5000/pi \
-H "Content-Type: application/json" \
-d '{"samples":1000000}'
```

### Histórico

```bash
curl http://127.0.0.1:5000/history
```

---

## Testes

```bash
pytest -v
```

Coverage:

```bash
pytest --cov=.
```

Coverage HTML:

```bash
pytest --cov=. --cov-report=html
xdg-open htmlcov/index.html
```

---

## Tecnologias

* Flask
* Redis
* TinyDB
* pytest
* pytest-cov
* SonarQube

---

## TODO

* adicionar Swagger/OpenAPI
* criar mais testes de integração
* adicionar Docker
* adicionar autenticação
* melhorar tratamento de erros


