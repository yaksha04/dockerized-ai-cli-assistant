import re
from typing import Optional, Dict

def parse_command(command_text: str) -> Optional[Dict]:
    command_text = command_text.lower().strip()

    # Match: create a new git branch called X
    match = re.search(r'create( a)?( new)?( git)? branch( called)? (\S+)', command_text)
    if match:
        branch_name = match.group(5)
        return {
            "action": "create_branch",
            "params": {"branch_name": branch_name}
        }

    # Match: delete the git branch X
    match = re.search(r'delete( the)?( git)? branch (\S+)', command_text)
    if match:
        branch_name = match.group(3)
        return {
            "action": "delete_branch",
            "params": {"branch_name": branch_name}
        }

    # Match: show disk usage
    if "show disk usage" in command_text:
        return {
            "action": "show_disk_usage",
            "params": {}
        }

    # Add more rules here

    return None



