import sys, os
import re
def get_file(file_name):
    # Example usage
    # PATH="/usr/bin:/usr/local/bin":"/usr/bin:/usr/local" ./your_shell.sh
    for path in os.environ["PATH"].split(os.pathsep):
        full_path = os.path.join(path, file_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return []
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
            # type abcd: abcd is in /usr/local/bin/abcd
            elif get_file(builtin_command)!=[]:
                sys.stdout.write(f"{builtin_command} is {get_file(builtin_command)}\n")
            else:
                sys.stdout.write(f"{builtin_command}: not found\n")
        # elif command.startswith('PATH'):
        #     paths, file_name=get_paths(comm=command)
        #     for path in paths:
        #         path_name = path + "/" + file_name
        #         try:
        #             os.popen(path_name)
        #         except:
        #             print("{path_name} file does not exist")
        else:
            sys.stdout.write(f"{command}: command not found\n")
        

if __name__ == "__main__":
    main()
