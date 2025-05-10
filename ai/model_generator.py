# ai/model_generator.py

import os
from rich import print
from openai import OpenAI
from google.generativeai import GenerativeModel
from anthropic import Anthropic

def generate_script(prompt: str, model: str = "openai") -> None:
    """Generate a script from an AI model based on the provided prompt."""
    print(f"[bold cyan]Generating script using model:[/bold cyan] {model}")
    
    if model == "openai":
        return _openai_generate(prompt)
    elif model == "google":
        return _google_generate(prompt)
    elif model == "anthropic":
        return _anthropic_generate(prompt)
    else:
        print(f"[red]❌ Unsupported model: {model}[/red]")

def _openai_generate(prompt: str) -> None:
    import openai
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    script = response.choices[0].message.content
    _write_script(prompt, script)

def _google_generate(prompt: str) -> None:
    model = GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    _write_script(prompt, response.text)

def _anthropic_generate(prompt: str) -> None:
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    _write_script(prompt, response.content[0].text)

def _write_script(prompt: str, code: str) -> None:
    import re
    from datetime import datetime

    safe_name = re.sub(r"\W+", "_", prompt.strip())[:50].lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_script_{safe_name}_{timestamp}.py"

    with open(filename, "w") as f:
        f.write(code)
    
    print(f"[green]✅ Script saved as:[/green] {filename}")
