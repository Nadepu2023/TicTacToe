import subprocess
import sys

def push_to_github(commit_msg):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    msg = "Quick commit from agentP"
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    push_to_github(msg)
