from core.parser import parse_command
from core.execution import execute_command

if __name__ == "__main__":
    while True:
        try:
            command = input(">>> ")
            if command.lower() in ["exit", "quit"]:
                break
            parsed = parse_command(command)
            print("Parsed:", parsed)
            execute_command(parsed)
        except KeyboardInterrupt:
            break




