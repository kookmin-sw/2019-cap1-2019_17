import subprocess
import os

def filesInput() -> tuple:
    ''' User interaction with the program. Returns a tuple of the inputs
        provided from the user. '''
    videoInput  = input("Input the YouTube link or name of your video: ")
    
    return videoInput

def OverWriting(audioFile: str, audioFile2: str):
    ''' If the audio file isnt in the directory, returns False as overwriting
        is then determined impossible. Otherwise, validates if the user
        is fine with the file being overwritten. If not, returns True. '''
    if directoryContains(audioFile):    # 디렉토리에 이미 같은 파일이 있으면
        os.remove(audioFile)            # 원본파일을 지움.
    if flacdirectoryContains(audioFile2):
        os.remove('./flac/' + audioFile2)


def directoryContains(audioFile: str) -> bool:
    ''' Returns True or False if the file is already in the directory to avoid overwriting.'''
    return audioFile in os.listdir()

def flacdirectoryContains(audioFile: str) -> bool:
    ''' Returns True or False if the file is already in the directory to avoid overwriting.'''
    return audioFile in os.listdir('./flac')


def youtubeLink(videoInput: str) -> bool:
    ''' Returns True if the input was from YouTube or False otherwise. '''
    return 'youtube' in videoInput


def youtubeDownload(user_link: str) -> None:
    ''' Downloads the video from YouTube if the user inputted a YouTube link. '''
    print('Downloading...')
    try:
        command = f"youtube-dl -f bestaudio --extract-audio --audio-format flac --audio-quality 0 {user_link}"
        subprocess.call(command, shell=True)
        videoInput = max(os.listdir(), key=os.path.getctime)
        os.rename(videoInput, 'immediate.flac')

    except os.error:
        print('Invalid characters used for File name. YouTube title is now File name.')
    
    print('Done Downloading..')

def convertAudio(audioInput: str, audioFile: str) -> None:
    print('Starting to Convert...')
    #  -ar : sample rate(default : 44100), -ab : bit rate (음질), -ac : audio channel
    command = f"ffmpeg -i {audioInput} -ab 192k -ac 2 -ar 44100 -vn {audioFile}"
    subprocess.call(command, shell=True)
    #os.remove(audioInput)
    
    print('DONE')


