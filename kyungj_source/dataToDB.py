# Mongo DB에 음성파일의 이름, keyword 3개, duration 업로드
# 음성파일: test.flac 
# 필요한 파일: test_keyword.txt & test_duration.txt 

# Pymongo install for Mac OS X
# $ sudo pip3 install pymongo

# Compile 방법
# $ python3 dataToDB.py test

import pymongo
import sys
import os.path
import subprocess
import time

# test_keyword.txt 파일이 있을 경우 실행
try:
    f = open(sys.argv[1] + "_keyword.txt")
except:
    print("wrong input")
    sys.exit[1]

# 파일 이름을 Mongo DB에 저장
connection = pymongo.MongoClient()
db = connection.test
collection = db.test_collection

post = {"filename" : sys.argv[1]}
collection.insert_one(post)

# test_keyword에서 keyword list를 만들어 Mongo DB에 저장
keywords = []
while True:
    line = f.readline()
    if not line:
        break
    keywords.append(line[:-1]) # \n 개행문자 삭제
f.close()

newvalues = { "$set" : {"keyword" : keywords}}
collection.update_one(post, newvalues) # 기존의 데이터에 추가

# 음성파일의 길이를 담고있는 test_duration을 읽어서 Mongo DB에 추가
duration = ''
with open(sys.argv[1] + '_duration.txt') as f:
    duration = f.read()

newvalues = { "$set" : {"duration" : duration}}
collection.update_one(post, newvalues)

# 현재 시간을 Mongo DB에 추가
uploadTime = time.strftime('%d %b %Y %H:%M ', time.localtime(time.time()))
newvalues = { "$set" : {"upload_time" : uploadTime[:-1]}}
test_collection.update_one(post, newvalues)