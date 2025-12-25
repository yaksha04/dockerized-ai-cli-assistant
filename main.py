from parser import parse_command
from execution import execute_command


def main():
    print("🤖 AI CLI Assistant started (type 'exit' or 'quit' to stop)\n")

    while True:
        try:
            command = input(">>> ").strip()

            if not command:
                continue

            if command.lower() in ("exit", "quit"):
                print("👋 Exiting AI CLI Assistant.")
                break

            parsed = parse_command(command)

            if not parsed:
                print("❌ Command not recognized.")
                continue

            execute_command(parsed)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting AI CLI Assistant.")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
