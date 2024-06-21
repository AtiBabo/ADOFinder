import datetime
import pytz
import os

class CCO:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CHECK = '\033[92m✓ \033[0m'
    RESET = '\033[0m'

class INFO:
    version = '0.0.1'
    default_color = 0x91b2e1
    eror_color = 0xFA6B5F
    uptime = str(int(datetime.datetime.now(pytz.timezone('Asia/Seoul')).timestamp()))
    now_directory = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉터리