import subprocess
import shutil
import psutil
import os


def execute_command(parsed):
    if not parsed:
        print("❌ Unknown command.")
        return

    action = parsed.get("action")
    params = parsed.get("params", {})

    # =========================
    # GIT COMMANDS
    # =========================

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
                print(
                    f"❌ Failed to delete Git branch '{branch_name}'. "
                    "It may not exist or isn't fully merged."
                )
        else:
            print("⚠️ No branch name provided.")

    # =========================
    # SYSTEM MONITORING
    # =========================

    elif action == "show_disk_usage":
        total, used, free = shutil.disk_usage("/")
        print(
            f"💾 Disk Usage:\n"
            f"  Total: {total // (2**30)} GB\n"
            f"  Used: {used // (2**30)} GB\n"
            f"  Free: {free // (2**30)} GB"
        )

    elif action == "cpu_usage":
        cpu = psutil.cpu_percent(interval=1)
        print(f"🧠 CPU Usage: {cpu}%")

    elif action == "memory_usage":
        mem = psutil.virtual_memory()
        print(f"🧠 Memory Usage: {mem.percent}%")

    # =========================
    # FILE & DIRECTORY COMMANDS
    # =========================

    elif action == "create_file":
        filename = params.get("filename")
        if filename:
            try:
                open(filename, "a").close()
                print(f"📄 File '{filename}' created successfully.")
            except Exception as e:
                print(f"❌ Failed to create file: {e}")
        else:
            print("⚠️ No filename provided.")

    elif action == "create_directory":
        dir_name = params.get("dir_name")
        if dir_name:
            try:
                os.makedirs(dir_name, exist_ok=True)
                print(f"📁 Directory '{dir_name}' created successfully.")
            except Exception as e:
                print(f"❌ Failed to create directory: {e}")
        else:
            print("⚠️ No directory name provided.")

    elif action == "delete_file":
        filename = params.get("filename")
        if filename:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                    print(f"🗑️ File '{filename}' deleted successfully.")
                except Exception as e:
                    print(f"❌ Failed to delete file: {e}")
            else:
                print("⚠️ File does not exist.")
        else:
            print("⚠️ No filename provided.")

    elif action == "list_files":
        try:
            files = os.listdir(".")
            print("📂 Files in current directory:")
            for f in files:
                print("  -", f)
        except Exception as e:
            print(f"❌ Failed to list files: {e}")

    elif action == "pwd":
        print(f"📍 Current Directory: {os.getcwd()}")

    # =========================
    # PERMISSIONS (CHMOD)
    # =========================

    elif action == "chmod":
        mode = params.get("mode")
        target = params.get("target")

        if mode and target:
            if os.path.exists(target):
                try:
                    subprocess.run(["chmod", mode, target], check=True)
                    print(f"🔐 Permissions {mode} set on '{target}'.")
                except subprocess.CalledProcessError:
                    print("❌ Failed to change permissions.")
            else:
                print("⚠️ Target file does not exist.")
        else:
            print("⚠️ Missing mode or target.")

    # =========================
    # FALLBACK
    # =========================

    else:
        print("⚠️ Action not implemented yet.")
