from lib import aimer
from lib import helpers
from lib import keycodes
from lib.bones import bones
import ctypes




fov = 0.1


distance_limit = 250


trigger = keycodes.RBUTTON



aim_locations = [bones['Neck']]


aim_switch = keycodes.END
#aim_switch = None


screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# or
#screensize = (1280, 960)





version = "0.5"

if fov < 0.1 or fov > 3.0:  # you can delete this if you know what you're doing
    print("Check your fov setting.")
    exit(1)
if distance_limit is not None and distance_limit <= 0:
    print("Check your distance_limit setting")
    exit(1)

if __name__ == "__main__":
    print("BFV AimBot Version %s" % version)
    print("""
    ____        _                __
   / __ \____ _(_)   _____  ____/ /
  / / / / __ `/ / | / / _ \/ __  / 
 / /_/ / /_/ / /| |/ /  __/ /_/ /  
/_____/\__,_/_/ |___/\___/\__,_/   """)

    if not helpers.is_admin():
        print("[x] Error: This must be run with admin privileges")
        input("Press Enter to continue...")
        exit(1)

    if not helpers.is_python3():
        print("- Error: This script requires Python 3")
        raw_input("Press Enter to continue...")
        exit(1)

    arch = helpers.get_python_arch()
    if arch != 64:
        print("- Error: This version of Python is not 64-bit")
        input("Press Enter to continue...")
        exit(1)

    print ("Using screensize: %s x %s" % screensize)
    aimer = aimer.Aimer(screensize, trigger, distance_limit, fov, aim_locations, aim_switch)
    aimer.start()

