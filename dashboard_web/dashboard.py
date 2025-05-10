# dashboard_web/dashboard.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from monitoring.disk_monitor import get_disk_usage_stats
from monitoring.memory_monitor import get_memory_usage_stats

app = FastAPI(title="FredFix Web Dashboard")

@app.get("/", response_class=HTMLResponse)
async def show_dashboard():
    disk = get_disk_usage_stats()
    memory = get_memory_usage_stats()
    return f"""
    <html>
        <head>
            <title>FredFix Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 2em; }}
                .section {{ margin-bottom: 2em; }}
                h1, h2 {{ color: #2c3e50; }}
            </style>
        </head>
        <body>
            <h1>FredFix System Dashboard</h1>

            <div class="section">
                <h2>Disk Usage</h2>
                <p>Total: {disk['total']} GB</p>
                <p>Used: {disk['used']} GB</p>
                <p>Free: {disk['free']} GB</p>
                <p>Usage: {disk['percent']}%</p>
            </div>

            <div class="section">
                <h2>Memory Usage</h2>
                <p>Total: {memory['total']} MB</p>
                <p>Used: {memory['used']} MB</p>
                <p>Free: {memory['free']} MB</p>
                <p>Usage: {memory['percent']}%</p>
            </div>
        </body>
    </html>
    """

def launch_dashboard(target: str = "disk"):
    import uvicorn
    uvicorn.run("dashboard_web.dashboard:app", host="127.0.0.1", port=8000, reload=False)
