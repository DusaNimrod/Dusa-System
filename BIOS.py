"""
(C) DUSA NIMROD 2024

DUSABIOS VERSION 1.0
-VERSION 1.0
-OPEN SOURCE



MIT License

Copyright (c) 2024 Dusa Nimrod

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import os
import time
import platform
from datetime import datetime
import subprocess

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

def show_system_info():
    print("System Information:")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    time.sleep(2)
    clear_screen()

def clear_screen_option():
    clear_screen()
    print(f"{TEXT_COLORS['green']}Screen cleared.{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()

def ping_test():
    host = input("Enter host (IP or domain): ")
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{TEXT_COLORS['green']}Ping to {host} successful!{TEXT_COLORS['default']}")
    else:
        print(f"{TEXT_COLORS['red']}Ping to {host} failed.{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()

def show_uptime():
    uptime = datetime.now() - datetime.fromtimestamp(os.path.getmtime('/proc/1'))
    print(f"System uptime: {str(uptime).split('.')[0]}")
    time.sleep(2)
    clear_screen()

def show_system_logs():
    try:
        with open("/var/log/syslog", "r") as log_file:
            logs = log_file.readlines()[-10:]
        print("Last 10 system logs:")
        for log in logs:
            print(log.strip())
    except FileNotFoundError:
        print(f"{TEXT_COLORS['red']}System log file not found.{TEXT_COLORS['default']}")
    except Exception as e:
        print(f"{TEXT_COLORS['red']}Error reading system logs: {e}{TEXT_COLORS['default']}")
    time.sleep(2)
    clear_screen()

def display_menu():
    print(f"""
{TEXT_COLORS['cyan']}======================================================
                    DusaBIOS v1.2
======================================================
 [1] {TEXT_COLORS['blue']}Reboot{TEXT_COLORS['default']}
 [2] {TEXT_COLORS['blue']}Exit{TEXT_COLORS['default']}
 [3] {TEXT_COLORS['blue']}Change Text Color{TEXT_COLORS['default']}
 [4] {TEXT_COLORS['blue']}Show Time{TEXT_COLORS['default']}
 [5] {TEXT_COLORS['blue']}System Info{TEXT_COLORS['default']}
 [6] {TEXT_COLORS['blue']}Clear Screen{TEXT_COLORS['default']}
 [7] {TEXT_COLORS['blue']}Ping Test{TEXT_COLORS['default']}
 [8] {TEXT_COLORS['blue']}Show Uptime{TEXT_COLORS['default']}
 [9] {TEXT_COLORS['blue']}Show System Logs{TEXT_COLORS['default']}
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
            show_system_info()
        elif choice == "6":
            clear_screen_option()
        elif choice == "7":
            ping_test()
        elif choice == "8":
            show_uptime()
        elif choice == "9":
            show_system_logs()
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
