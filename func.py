import requests
import os
from getpass import getuser as usr
from tqdm import tqdm
import ctypes

from config import *

ctypes.windll.kernel32.SetConsoleTitleW(installertitle)

def begin():
    print('Downloading your files...')
    IURL = url
    response = requests.get(IURL, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('C:/Users/' + usr() + '/Documents/' + defaultdirname + '/' + filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print(errormessage)
        os.remove('C:/Users/' + usr() + '/Documents/' + defaultdirname + '/' + filename)
    else:
        print('Download finished. File is stored in: C:/Users/' + usr() + '/Documents/' + defaultdirname)
        input('Press any key to exit...')