import subprocess
import shutil
import psutil

def execute_command(parsed):
    if not parsed:
        print("Unknown command.")
        return

    action = parsed.get("action")
    params = parsed.get("params", {})

    if action == "create_branch":
        branch_name = params.get("branch_name")
        if branch_name:
            try:
                subprocess.run(["git", "checkout", "-b", branch_name], check=True)
                print(f"✅ Git branch '{branch_name}' created successfully.")
            except subprocess.CalledProcessError:
                print("❌ Failed to create Git branch.")
        else:
            print("⚠️ No branch name provided.")

    elif action == "delete_branch":
        branch_name = params.get("branch_name")
        if branch_name:
            try:
                subprocess.run(["git", "branch", "-d", branch_name], check=True)
                print(f"🗑️ Git branch '{branch_name}' deleted successfully.")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to delete Git branch '{branch_name}'. It may not exist or isn't fully merged.")
        else:
            print("⚠️ No branch name provided.")

    elif action == "show_disk_usage":
        total, used, free = shutil.disk_usage("/")
        print(f"💾 Disk Usage:\n  Total: {total // (2**30)} GB\n  Used: {used // (2**30)} GB\n  Free: {free // (2**30)} GB")

    else:
        print("⚠️ Action not implemented yet.")

