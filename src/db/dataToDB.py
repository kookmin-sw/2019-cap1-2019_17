# Mongo DB에 음성파일의 이름, keyword 5개, duration 업로드
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
from pymongo import MongoClient

connection = MongoClient()
db = connection.summer
summer_collection = db.summer_collection

# test_keyword.txt 파일이 있을 경우 실행
try:
    f = open(sys.argv[1] + "_keyword.txt")
except:
    print("wrong input")
    sys.exit[1]

# 파일 이름을 Mongo DB에 저장
post = {"filename" : sys.argv[1]}
summer_collection.insert_one(post)

# test_keyword에서 keyword list를 만들어 Mongo DB에 저장
keyword = []
while True:
    line = f.readline()
    if not line:
        break
    keyword.append(line[:-1]) # \n 개행문자 삭제
f.close()

newvalues = { "$set" : {"keyword" : keyword}}
summer_collection.update_one(post, newvalues) # 기존의 데이터에 추가

# 음성파일의 길이를 담고있는 test_duration을 읽어서 Mongo DB에 추가
duration = ''
with open(sys.argv[1] + '_duration.txt') as f:
    duration = f.read()

newvalues = { "$set" : {"duration" : duration}}
summer_collection.update_one(post, newvalues)

uploaded = time.strftime('%d %b %Y %H:%M ', time.localtime(time.time()))
newvalues = { "$set" : {"uploaded" : uploaded[:-1]}}
summer_collection.update_one(post, newvalues)

