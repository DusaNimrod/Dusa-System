import os
import time
import platform
from BIOS import main_menu, clear_screen, TEXT_COLORS

def boot_animation():
    clear_screen()
    print(f"{TEXT_COLORS['cyan']}Initializing Bootloader...{TEXT_COLORS['default']}")
    time.sleep(1)

    for i in range(1, 4):
        print(f"{TEXT_COLORS['yellow']}Loading system files... ({i}/3){TEXT_COLORS['default']}")
        time.sleep(1)

    print(f"{TEXT_COLORS['green']}Bootloader Complete.{TEXT_COLORS['default']}")
    time.sleep(1)
    clear_screen()

def system_check():
    print(f"{TEXT_COLORS['yellow']}Performing system checks...{TEXT_COLORS['default']}")
    time.sleep(1)

    checks = [
        "Memory check",
        "CPU check",
        "File system integrity",
        "BIOS configuration"
    ]

    for check in checks:
        print(f"{TEXT_COLORS['blue']}{check}... OK{TEXT_COLORS['default']}")
        time.sleep(0.5)

    print(f"{TEXT_COLORS['green']}All systems are operational.{TEXT_COLORS['default']}")
    time.sleep(1)

def boot_bios():
    print(f"{TEXT_COLORS['magenta']}Launching DusaBIOS...{TEXT_COLORS['default']}")
    time.sleep(1)
    clear_screen()
    main_menu()

if __name__ == "__main__":
    boot_animation()
    system_check()
    boot_bios()
