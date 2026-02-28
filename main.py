from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# ✅ ОДИН обработчик для главной страницы с HTML
@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI + Nginx</title>
        <style>
            body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                   min-height: 100vh; display: flex; justify-content: center; align-items: center; }
            .card { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            .success { color: #48bb78; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 FastAPI + Nginx + Docker</h1>
            <p class="success">✅ Приложение работает!</p>
            <p>Текущее время: <span id="time"></span></p>
            <p>Статус: <span id="status"></span></p>
            <button onclick="checkAPI()">Проверить API</button>
            <pre id="result"></pre>
        </div>
        
        <script>
            document.getElementById('time').textContent = new Date().toLocaleString();
            document.getElementById('status').textContent = 'онлайн';
            
            async function checkAPI() {
                try {
                    const response = await fetch('/api/hello');
                    const data = await response.json();
                    document.getElementById('result').textContent = 
                        JSON.stringify(data, null, 2);
                } catch (error) {
                    document.getElementById('result').textContent = 
                        'Ошибка: ' + error.message;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# ✅ Исправлен путь (со слешем)
@app.get("/health")
async def health():
    return {"status": "ok"}

# ✅ API endpoint
@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI"}
