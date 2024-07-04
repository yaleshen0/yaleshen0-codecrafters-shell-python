import sys


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command=input()
        if command == 'exit 0':
            break
        if command.startswith('echo'):
            parts=command.split(" ", 1)
            echo_command=parts[0]
            message = parts[1]
            sys.stdout.write(f"{message}\n")
        elif command.startswith('type'):
            parts=command.split(" ")
            type_command = parts[0]
            builtin_command = parts[1]
            if builtin_command in ('echo', 'exit', 'type'):
                sys.stdout.write(f"{builtin_command} is a shell builtin\n")
            else:
                sys.stdout.write(f"{builtin_command}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")
        

if __name__ == "__main__":
    main()
