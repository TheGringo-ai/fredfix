import argparse
import sys
from rich import print

from scripts.check_envs import check_envs
from ai.model_generator import generate_script
from monitoring.disk_monitor import monitor_disk
from monitoring.memory_monitor import get_memory_usage_stats as monitor_memory
from dashboard_web.dashboard import launch_dashboard


def main():
    parser = argparse.ArgumentParser(description="FredFix CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Doctor
    subparsers.add_parser("doctor", help="Run environment checks")

    # Model
    model_parser = subparsers.add_parser("model", help="Generate script from prompt")
    model_parser.add_argument("prompt", type=str, help="Prompt to send to AI")
    model_parser.add_argument(
        "--model", type=str, default="openai", help="Model backend to use"
    )

    # Monitor
    monitor_parser = subparsers.add_parser("monitor", help="Run a system monitor")
    monitor_parser.add_argument(
        "target", choices=["disk", "memory"], help="What to monitor"
    )

    # Dashboard
    dashboard_parser = subparsers.add_parser("dashboard", help="Launch a terminal dashboard")
    dashboard_parser.add_argument(
        "target", choices=["disk", "memory"], help="Which dashboard to show"
    )

    args = parser.parse_args()

    if args.command == "doctor":
        check_envs()

    elif args.command == "model":
        generate_script(prompt=args.prompt, model=args.model)

    elif args.command == "monitor":
        if args.target == "disk":
            monitor_disk()
        elif args.target == "memory":
            stats = monitor_memory()
            print("[bold cyan]Memory Stats:[/bold cyan]")
            for k, v in stats.items():
                print(f"{k}: {v}")

    elif args.command == "dashboard":
        launch_dashboard(args.target)

    else:
        print("[red]❌ Unknown or missing command. Use --help for options.[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
