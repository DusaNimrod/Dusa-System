"""
2024 DUSA SYSTEM (C)
THIS PROJECT WAS MADE WITH PYTHON
BUILT IN COMMANDS:

help           version        exit           clear          
showtime       reverse        status         user           
date           hostname       whoami         listdir        
pwd            mkdir          rmdir          touch          
cat            echo           chdir          env            
repeat         

"""



import os
import time
import sys

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
        "status", "user", "date", "hostname", "whoami", "listdir",
        "pwd", "mkdir", "rmdir", "touch", "cat", "echo", "chdir",
        "env", "repeat"
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
        elif command == "hostname":
            print(os.uname()[1])
        elif command == "whoami":
            print(username)
        elif command == "listdir":
            print("\n".join(os.listdir(".")))
        elif command == "pwd":
            print(os.getcwd())
        elif command.startswith("mkdir"):
            try:
                parts = command.split(" ", 1)
                os.mkdir(parts[1])
                print(f"Directory '{GREEN}{parts[1]}{RESET}' created.")
            except IndexError:
                print("Error: Directory name not provided.")
            except FileExistsError:
                print(f"Error: Directory '{GREEN}{parts[1]}{RESET}' already exists.")
        elif command.startswith("rmdir"):
            try:
                parts = command.split(" ", 1)
                os.rmdir(parts[1])
                print(f"Directory '{GREEN}{parts[1]}{RESET}' removed.")
            except IndexError:
                print("Error: Directory name not provided.")
            except FileNotFoundError:
                print(f"Error: Directory '{GREEN}{parts[1]}{RESET}' not found.")
        elif command.startswith("touch"):
            try:
                parts = command.split(" ", 1)
                with open(parts[1], 'w') as f:
                    pass
                print(f"File '{GREEN}{parts[1]}{RESET}' created.")
            except IndexError:
                print("Error: File name not provided.")
        elif command.startswith("cat"):
            try:
                parts = command.split(" ", 1)
                with open(parts[1], 'r') as f:
                    print(f.read())
            except IndexError:
                print("Error: File name not provided.")
            except FileNotFoundError:
                print(f"Error: File '{GREEN}{parts[1]}{RESET}' not found.")
        elif command.startswith("echo"):
            parts = command.split(" ", 1)
            if len(parts) > 1:
                print(parts[1])
            else:
                print("Error: No string provided to echo.")
        elif command.startswith("chdir"):
            try:
                parts = command.split(" ", 1)
                os.chdir(parts[1])
                print(f"Changed directory to {GREEN}{parts[1]}{RESET}")
            except IndexError:
                print("Error: Directory path not provided.")
            except FileNotFoundError:
                print(f"Error: Directory '{GREEN}{parts[1]}{RESET}' not found.")
        elif command == "env":
            for key, value in os.environ.items():
                print(f"{GREEN}{key}{RESET}: {value}")
        elif command.startswith("repeat"):
            try:
                parts = command.split(" ", 2)
                string = parts[1]
                times = int(parts[2])
                print(string * times)
            except IndexError:
                print("Error: String or repeat count not provided.")
            except ValueError:
                print("Error: Please provide a valid number for repeat count.")
        elif command == "":
            pass  
        else:
            print(f"Command '{GREEN}{command}{RESET}' is not recognized.")

Terminal()
