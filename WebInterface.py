from fastapi import *
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_main_page():
    html_page = """<!DOCTYPE html>
<html>
<head>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body, iframe { margin:0; padding:0; width:100%; height:100vh; border:none; }
    </style>
</head>
<body>
    <iframe src="https://www.deepseek.com/"></iframe>
    <script>
        Telegram.WebApp.expand();
    </script>
</body>
</html>"""

    return html_page
