import os
import time
import platform
import subprocess
from datetime import datetime

TEXT_COLORS = {
    "default": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "cyan": "\033[36m",
    "magenta": "\033[35m"
}

bios_status = {
    "text_color": "default",
    "restart_count": 0
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def change_text_color():
    print("Available colors: red, green, yellow, blue, cyan, magenta, default")
    color = input("Choose a color: ").strip().lower()
    if color in TEXT_COLORS:
        bios_status["text_color"] = color
        print(f"{TEXT_COLORS[color]}Text color changed to {color}.{TEXT_COLORS['default']}")
    else:
        print(f"{TEXT_COLORS['red']}Invalid color choice.{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()

def show_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")
    time.sleep(2)
    clear_screen()

def reboot():
    bios_status["restart_count"] += 1
    print(f"{TEXT_COLORS['yellow']}Rebooting...{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()
    main_menu()

def exit_bios():
    exit()

def load_dusa_system():
    print(f"{TEXT_COLORS['cyan']}Loading Dusa System...{TEXT_COLORS['default']}")
    time.sleep(1)
    if os.path.exists("System.py"):
        try:
            subprocess.run(["python", "System.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"{TEXT_COLORS['red']}Error running Dusa System: {e}{TEXT_COLORS['default']}")
        except Exception as e:
            print(f"{TEXT_COLORS['red']}Unexpected error: {e}{TEXT_COLORS['default']}")
    else:
        print(f"{TEXT_COLORS['red']}ERROR: COULDN'T FIND System.py{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()

def display_menu():
    print(f"""
{TEXT_COLORS['cyan']}======================================================
                    DusaBIOS v1.3
======================================================
 [1] {TEXT_COLORS['blue']}Reboot{TEXT_COLORS['default']}
 [2] {TEXT_COLORS['blue']}Exit{TEXT_COLORS['default']}
 [3] {TEXT_COLORS['blue']}Change Text Color{TEXT_COLORS['default']}
 [4] {TEXT_COLORS['blue']}Show Time{TEXT_COLORS['default']}
 [5] {TEXT_COLORS['blue']}System Info{TEXT_COLORS['default']}
 [6] {TEXT_COLORS['blue']}Clear Screen{TEXT_COLORS['default']}
 [7] {TEXT_COLORS['blue']}Ping Test{TEXT_COLORS['default']}
 [8] {TEXT_COLORS['blue']}Load Dusa System{TEXT_COLORS['default']}
======================================================
{TEXT_COLORS['yellow']}Please choose an option from the menu above:{TEXT_COLORS['default']}
""")

def main_menu():
    while True:
        display_menu()
        choice = input("> ").strip()
        
        if choice == "1":
            reboot()
        elif choice == "2":
            exit_bios()
        elif choice == "3":
            change_text_color()
        elif choice == "4":
            show_time()
        elif choice == "5":
            print("System Information:")
            print(f"OS: {platform.system()} {platform.release()}")
            print(f"Version: {platform.version()}")
            time.sleep(2)
            clear_screen()
        elif choice == "6":
            clear_screen()
            print(f"{TEXT_COLORS['green']}Screen cleared.{TEXT_COLORS['default']}")
            time.sleep(2)
            clear_screen()
        elif choice == "7":
            print(f"{TEXT_COLORS['yellow']}Pinging localhost...{TEXT_COLORS['default']}")
            os.system("ping -c 4 127.0.0.1")
            time.sleep(2)
            clear_screen()
        elif choice == "8":
            load_dusa_system()
        else:
            print(f"{TEXT_COLORS['red']}Invalid choice. Try again.{TEXT_COLORS['default']}")
            time.sleep(2)
            clear_screen()

if __name__ == "__main__":
    clear_screen()
    print(f"{TEXT_COLORS['cyan']}Loading DusaBIOS...{TEXT_COLORS['default']}")
    time.sleep(1)
    clear_screen()
    main_menu()

