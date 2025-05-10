# monitoring/disk_monitor.py

import psutil
from rich import print

def monitor_disk():
    """Display current disk usage statistics."""
    usage = psutil.disk_usage("/")
    
    print("\n[bold cyan]💽 Disk Usage Report[/bold cyan]")
    print(f"📦 Total: {usage.total / (1024 ** 3):.2f} GB")
    print(f"📈 Used:  {usage.used / (1024 ** 3):.2f} GB")
    print(f"📉 Free:  {usage.free / (1024 ** 3):.2f} GB")
    print(f"📊 Usage: {usage.percent}%\n")

def get_disk_usage_stats():
    """Return disk usage as a dictionary (for API/dashboard use)."""
    usage = psutil.disk_usage("/")
    return {
        "total": f"{usage.total / (1024 ** 3):.2f} GB",
        "used": f"{usage.used / (1024 ** 3):.2f} GB",
        "free": f"{usage.free / (1024 ** 3):.2f} GB",
        "percent": usage.percent
    }
