from adityacli.terminal_tool import run_command
from adityacli.ui import console

def git_status():
    return run_command("git status")

def git_diff():
    return run_command("git diff")

def git_log():
    return run_command("git log --oneline -10")

def git_branch():
    return run_command("git branch")

def display_command_result(result):
    if result["success"]:
        console.print(result["stdout"])
    else:
        console.print(result["stderr"])