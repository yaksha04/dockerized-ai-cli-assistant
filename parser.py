import re
from typing import Optional, Dict


def parse_command(command_text: str) -> Optional[Dict]:
    command_text = command_text.lower().strip()

    # =========================
    # GIT COMMANDS
    # =========================

    # Create git branch
    match = re.search(r'create( a)?( new)?( git)? branch( called)? (\S+)', command_text)
    if match:
        return {
            "action": "create_branch",
            "params": {"branch_name": match.group(5)}
        }

    # Delete git branch
    match = re.search(r'delete( the)?( git)? branch (\S+)', command_text)
    if match:
        return {
            "action": "delete_branch",
            "params": {"branch_name": match.group(3)}
        }

    # =========================
    # SYSTEM MONITORING
    # =========================

    # Disk usage
    if "show disk usage" in command_text:
        return {
            "action": "show_disk_usage",
            "params": {}
        }

    # =========================
    # FILE & DIRECTORY COMMANDS
    # =========================

    # Create file
    match = re.search(r'create( a)? file (\S+)', command_text)
    if match:
        return {
            "action": "create_file",
            "params": {"filename": match.group(2)}
        }

    # Create directory / folder
    match = re.search(r'create( a)? (directory|folder) (\S+)', command_text)
    if match:
        return {
            "action": "create_directory",
            "params": {"dir_name": match.group(3)}
        }

    # Delete file
    match = re.search(r'delete file (\S+)', command_text)
    if match:
        return {
            "action": "delete_file",
            "params": {"filename": match.group(1)}
        }

    # List files
    if "list files" in command_text or "show files" in command_text:
        return {
            "action": "list_files",
            "params": {}
        }

    # Show current directory
    if "current directory" in command_text or "where am i" in command_text:
        return {
            "action": "pwd",
            "params": {}
        }

    # =========================
    # PERMISSIONS (CHMOD)
    # =========================

    # Give execute permission
    match = re.search(r'give execute permission to (\S+)', command_text)
    if match:
        return {
            "action": "chmod",
            "params": {
                "mode": "755",
                "target": match.group(1)
            }
        }

    # Set numeric permission
    match = re.search(r'set permission (\d{3}) on (\S+)', command_text)
    if match:
        return {
            "action": "chmod",
            "params": {
                "mode": match.group(1),
                "target": match.group(2)
            }
        }

    # =========================
    # FALLBACK
    # =========================

    return None
