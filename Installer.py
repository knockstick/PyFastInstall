import time
import os
from getpass import getuser as usr

from config import *
from func import begin

try:
    os.mkdir('C:/Users/' + usr() + '/Documents/' + defaultdirname)
except:
    pass

print('Welcome to ' + programname + ' installation program!')
print('Install will begin in 3 seconds...')
time.sleep(installdelay)
print('')
begin()
