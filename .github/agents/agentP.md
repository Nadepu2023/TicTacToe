# agentP

## Purpose
A simple workflow to push your code changes to GitHub using a single command.

## Usage
Whenever you want to push your latest code changes, run the following command in your project directory:

```
sh agentP.sh
```

Or, if you want to use a custom commit message:

```
sh agentP.sh "Your commit message here"
```

## Setup
1. Make sure you have already set up your GitHub repository and added it as a remote (usually named `origin`).
2. Place the `agentP.sh` script (see below) in your project root directory.
3. Make the script executable (run `chmod +x agentP.sh` in the terminal).

## agentP.sh Script
```
#!/bin/bash

# Usage: sh agentP.sh "commit message"

COMMIT_MSG=${1:-"Quick commit from agentP"}

git add .
git commit -m "$COMMIT_MSG"
git push origin main
```

---

> Tip: You can type `.agentP` as a reminder in your code or notes, but you must run the script in the terminal to actually push your changes.
