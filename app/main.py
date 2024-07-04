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
        else:
            sys.stdout.write(f"{command}: command not found\n")
        

if __name__ == "__main__":
    main()
