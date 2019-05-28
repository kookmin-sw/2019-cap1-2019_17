# get the length of audio file in python

# Ubuntu install 
# $ sudo apt install sox

# $ python3 getDuation.py test.flac
import subprocess
import sys

fileName = sys.argv[1] # file name
duration = str(subprocess.check_output('sox --info -d ' + fileName, shell=True))
duration = duration[2:]
duration = duration[:-6]

with open(fileName[:-5] + '_duration.txt', 'w') as f:
    f.write(duration)