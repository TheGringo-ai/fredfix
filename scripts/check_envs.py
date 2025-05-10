# scripts/check_envs.py

def check_envs():
    import os
    from rich import print

    required_vars = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GOOGLE_API_KEY",
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print(f"[red]❌ Missing env vars: {', '.join(missing)}[/red]")
    else:
        print("[green]✅ All required environment variables are set.[/green]")
