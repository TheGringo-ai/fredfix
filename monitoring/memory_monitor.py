# monitoring/memory_monitor.py

import psutil

def get_memory_usage_stats():
    """Returns memory usage statistics as a dictionary."""
    memory = psutil.virtual_memory()

    stats = {
        "total": round(memory.total / (1024 * 1024)),   # MB
        "used": round(memory.used / (1024 * 1024)),     # MB
        "free": round(memory.available / (1024 * 1024)),# MB
        "percent": memory.percent                       # Usage %
    }

    return stats

if __name__ == "__main__":
    from rich import print
    from rich.pretty import pprint

    pprint(get_memory_usage_stats())
