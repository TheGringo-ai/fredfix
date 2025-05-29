# AI GENERATED CODE: FredFix Assistant core logic
import openai
import os
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_git_diff():
    """Grab the last commit diff for AI analysis."""
    try:
        diff = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD"], text=True)
        return diff.strip()
    except subprocess.CalledProcessError as e:
        return f"Error getting diff: {e}"

def main():
    git_diff = get_git_diff()
    if not git_diff:
        print("No changes detected.")
        return

    prompt = f"""
You are FredFix, an elite AI dev assistant. Below is the latest code diff in this repository.
Review the changes, suggest improvements, spot bugs, and explain anything noteworthy.

Git diff:
{git_diff}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print("===== FredFix AI Response =====")
    print(response['choices'][0]['message']['content'])
    print("================================")

if __name__ == "__main__":
    main()