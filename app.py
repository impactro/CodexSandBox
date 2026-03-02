from datetime import datetime
from html import escape

from flask import Flask

app = Flask(__name__)

# Buffer cíclico em memória (máximo de 100 mensagens)
LOGS = []
MAX_LOGS = 100


def salvar_log(texto):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    LOGS.append(f"{horario} - {texto}")
    if len(LOGS) > MAX_LOGS:
        LOGS.pop(0)


def pagina_logs():
    recentes = list(reversed(LOGS))
    itens = "".join([f"<li>{escape(linha)}</li>" for linha in recentes])
    if not itens:
        itens = "<li>Nenhum log ainda.</li>"

    return f"""
    <html>
      <head><meta charset='utf-8'><title>Logs</title></head>
      <body>
        <h1>Página de logs (últimas {MAX_LOGS} mensagens)</h1>
        <ul>{itens}</ul>
      </body>
    </html>
    """


@app.get("/")
def index():
    salvar_log("GET /")
    return "Serviço no ar"


@app.get("/logs")
def logs():
    salvar_log("GET /logs")
    return pagina_logs()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
