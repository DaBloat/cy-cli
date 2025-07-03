import logging
from wallpaper import *
logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] @ %(module)s - %(message)s")

def boot():
    boot_wallpaper()

if __name__ == "__main__":
    boot()