import os
from ai.model_generator import generate_script

# A curated batch of prompts for mass-generation
model_prompts = [
    "Write a Python script to scan for large files over 1GB in the home directory.",
    "Generate a shell script to backup the ~/Documents folder to an external drive.",
    "Create a script that logs CPU usage every minute and alerts if over 90%.",
    "Write a script to monitor network latency to google.com and log spikes.",
    "Build a tool to clean up temporary files and empty the trash.",
    "Create a script to display active Python virtual environments.",
    "Generate a watchdog script that restarts a crashed process.",
    "Write a script that syncs a local folder with a remote S3 bucket.",
    "Generate a CLI that compresses and encrypts a folder using AES.",
    "Write a diagnostic script that checks disk, CPU, RAM, and GPU info.",
    "Create a Python script to check for failed cron jobs in the last 24 hours.",
    "Generate a cross-platform clipboard manager with history logging.",
    "Write a tool that finds and reports broken symlinks in the system.",
    "Build a script to display top 5 memory-hungry processes every hour.",
    "Create a tool to batch rename files in a directory using regex rules."
]

def generate_all_prompts(model="openai"):
    """Run through all batch prompts and generate scripts."""
    print(f"\n🚀 Starting batch generation with {model}...\n")
    for prompt in model_prompts:
        print(f"📌 Prompt: {prompt}")
        try:
            generate_script(prompt, model=model)
        except Exception as e:
            print(f"❌ Failed on: {prompt}\n{e}\n")
