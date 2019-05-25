# 음성파일의 길이를 구하기

# Ubuntu install 
# $ sudo apt install sox

# $ python3 getDuation.py test.flac

import subprocess
import sys

# 음성파일의 길이를 구해서 test_duration.txt에 쓰기
fileName = sys.argv[1] # file name
duration = str(subprocess.check_output('sox --info -d ' + fileName, shell=True))
duration = duration[2:]
duration = duration[:-6]

with open(fileName[:-5] + '_duration.txt', 'w') as f:
    f.write(duration)