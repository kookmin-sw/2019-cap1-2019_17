# get the length of audio file in python
import subprocess

# audioFile = '/Users/kyungj/gcloud/resources/test.flac'
audioFile = '/Users/kyungj/gcloud/resources/Google_Gnome.wav' # test audio
duration = str(subprocess.check_output('sox --info -d ' + audioFile, shell=True))
duration = duration[2:]
duration = duration[:-6]
print(duration)