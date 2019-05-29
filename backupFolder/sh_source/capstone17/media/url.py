import audio_extractor2 as audio
import sys

# argv[1] : url
# argv[2] : output file name
# python3  url.py url filenmae(확장자x)

def main():
    url = sys.argv[1]
    output_file_name = sys.argv[2]
    # print(url)
    # print(output_file_name)

    #videoInput = audio.filesInput()

    # YouTube links are handled different as requires a download
    if audio.youtubeLink(url):           # youtube 링크가 맞는지 검사.
        #audio.OverWriting(file_name, 'convert-result.flac')  # 전에 있던 file_name.flac, convert-result.flac 파일 삭제.
        audio.youtubeDownload(url)       # url에 있는 youtube 비디오 다운로드.
        audio.convertAudio('immediate.flac', output_file_name+'.flac') # 형식에 맞게 convert.
        #shutil.move('convert-result.flac', 'flac')    # 저장된 파일을 flac 폴더에 이동.

    # YouTube 링크가 유효하지 않는 경우.
    else:
        # 에러메세지
        print('이 링크는 유효하지 않습니다.')
        return


if __name__ == '__main__':
    main()