# API Python bem simples (Flask + log cíclico)

Esse exemplo tem só o básico:

- `GET /` → responde `Serviço no ar`
- `GET /logs` → mostra uma página HTML com logs em memória

## Log cíclico

- O log fica em um array em memória.
- Guarda no máximo **100 mensagens**.
- Quando passar de 100, remove a mais antiga.

## Rodar

```bash
pip install -r requirements.txt
python app.py
```

Abra no navegador:

- http://localhost:5000/
- http://localhost:5000/logs
