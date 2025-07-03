import shutil
import subprocess
import logging

logger = logging.getLogger(__name__)
SWWW = shutil.which('swww')
PACMAN = shutil.which('pacman')

def check_swww():
    '''Checking the availability of the swww package, install it if not available'''
    if SWWW is None:
        logger.warning('swww is not available!')
        logger.info('Installing through pacman...')
        p = subprocess.Popen(['sudo','pacman', '--noconfirm', '-S', 'swww'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        data = p.communicate()
        data = {"code": p.returncode, "stdout": data[0].decode(),
                    "stderr": data[1].rstrip(b'\n').decode()}
        logger.info('Installation Done!')
    else:
        logger.info('swww is available!')
        
def check_daemon():
    '''checking the status of the swww daemon, run if not active'''
    try:
        pid = subprocess.check_output(['pgrep', 'swww-daemon'])
        logger.info(f'swww-daemon already running @ {int(pid)}')
    except subprocess.CalledProcessError as e:
        logger.warning('swww-daemon is not active...')
        logger.info('swww-daemon is starting...')
        p = subprocess.Popen(['swww-daemon -q'], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        pid = subprocess.check_output(['pgrep', 'swww-daemon'])
        logger.info(f'swww-daemon already running @ {int(pid)}')

def boot_wallpaper():
    'Collective Functions to run the wallpaper'
    check_swww()
    check_daemon()

if __name__ == '__main__':
    boot_wallpaper()