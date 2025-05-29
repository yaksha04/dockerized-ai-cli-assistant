import subprocess
import shutil
import psutil

def execute_command(parsed):
    action = parsed.get("action")
    params = parsed.get("params", {})

    if action == "create_branch":
        branch = params.get("branch_name")
        return run_git_command(["git", "checkout", "-b", branch])

    elif action == "delete_branch":
        branch = params.get("branch_name")
        return run_git_command(["git", "branch", "-d", branch])

    elif action == "show_disk_usage":
        return get_disk_usage()

    else:
        return "Unknown action."


def run_git_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Git Error: {e}"

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return f"Disk Usage: {usage.percent}% used of {round(usage.total / 1e9, 2)} GB"

