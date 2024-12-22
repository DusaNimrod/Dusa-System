import os
import time
import sys

# ANSI escape codes for coloring
GREEN = "\033[32m"
RESET = "\033[0m"

def loading_screen():
    print("Booting up...")
    for _ in range(20):
        sys.stdout.write(GREEN + "#" + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def print_help():
    commands = [
        "help", "version", "exit", "clear", "showtime", "reverse",
        "status", "user", "date", "createdir", "removedir", "read",
        "showfiles", "location", "writefile", "appendfile",
        "deletefile", "renamefile", "change"
    ]
    col_width = 15
    cols_per_row = 4
    print("Available commands:")
    for i, cmd in enumerate(commands):
        print(cmd.ljust(col_width), end="")
        if (i + 1) % cols_per_row == 0:
            print()
    print()

def Terminal():
    loading_screen()

    print("======================")
    print("     Dusa System      ")
    print("======================")
    username = input("Login: ").strip()

    while True:
        command = input(f"{username}{GREEN}> {RESET}").strip().lower()

        if command == "help":
            print_help()
        elif command == "version":
            print("Dusa System version 1.0")
        elif command == "exit":
            break
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command == "showtime":
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
        elif command.startswith("reverse"):
            try:
                parts = command.split(" ", 1)
                string = parts[1]
                print(f"Reversed: {GREEN}{string[::-1]}{RESET}")
            except IndexError:
                print("Error: No string provided to reverse.")
        elif command == "status":
            print("System is running smoothly.")
        elif command == "user":
            print(f"Current user: {username}")
        elif command == "date":
            print(time.strftime("%Y-%m-%d"))
        elif command == "createdir":
            try:
                dirname = input("Enter directory name: ").strip()
                os.mkdir(dirname)
                print(f"Directory '{GREEN}{dirname}{RESET}' created.")
            except FileExistsError:
                print(f"Error: Directory '{GREEN}{dirname}{RESET}' already exists.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "removedir":
            try:
                dirname = input("Enter directory name: ").strip()
                os.rmdir(dirname)
                print(f"Directory '{GREEN}{dirname}{RESET}' removed.")
            except FileNotFoundError:
                print(f"Error: Directory '{GREEN}{dirname}{RESET}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "read":
            try:
                filename = input("Enter file name: ").strip()
                with open(filename, 'r') as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"Error: File '{GREEN}{filename}{RESET}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "showfiles":
            print("\n".join(os.listdir(".")))
        elif command == "location":
            print(os.getcwd())
        elif command == "writefile":
            try:
                filename = input("Enter file name: ").strip()
                content = input("Enter content: ").strip()
                with open(filename, 'w') as f:
                    f.write(content)
                print(f"File '{GREEN}{filename}{RESET}' created and written to.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "appendfile":
            try:
                filename = input("Enter file name: ").strip()
                content = input("Enter content: ").strip()
                with open(filename, 'a') as f:
                    f.write(content + "\n")
                print(f"Content appended to '{GREEN}{filename}{RESET}'.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "deletefile":
            try:
                filename = input("Enter file name: ").strip()
                os.remove(filename)
                print(f"File '{GREEN}{filename}{RESET}' deleted.")
            except FileNotFoundError:
                print(f"Error: File '{GREEN}{filename}{RESET}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "renamefile":
            try:
                old_name = input("Enter current file name: ").strip()
                new_name = input("Enter new file name: ").strip()
                os.rename(old_name, new_name)
                print(f"File renamed from '{GREEN}{old_name}{RESET}' to '{GREEN}{new_name}{RESET}'.")
            except FileNotFoundError:
                print(f"Error: File '{GREEN}{old_name}{RESET}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "change":
            try:
                new_dir = input("Enter new directory: ").strip()
                os.chdir(new_dir)
                print(f"Changed directory to '{GREEN}{new_dir}{RESET}'.")
            except FileNotFoundError:
                print(f"Error: Directory '{GREEN}{new_dir}{RESET}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "":
            pass
        else:
            print(f"Command '{GREEN}{command}{RESET}' is not recognized.")

Terminal()


