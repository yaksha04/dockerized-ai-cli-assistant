from core.parser import parse_command

while True:
    try:
        text = input(">>> ")
        if text.lower() in ["exit", "quit"]:
            break

        result = parse_command(text)
        if result:
            print("Parsed Command:", result)
        else:
            print("Unknown command.")
    except Exception as e:
        print("Error:", e)
from core.parser import parse_command

while True:
    try:
        text = input(">>> ")
        if text.lower() in ["exit", "quit"]:
            break

        result = parse_command(text)
        if result:
            print("Parsed Command:", result)
        else:
            print("Unknown command.")
    except Exception as e:
        print("Error:", e)



