# >>> python3 addFilename2Mongo.py filename
import pymongo
import sys
import os.path

connection = pymongo.MongoClient() # localhost 27017
db = connection.test # connection.${DB name}
test_collection = db.book # db.${collection name}

try:
    f = open(sys.argv[1] + '_summary.txt')  # filename + '_summary.txt'가 존재할 경우 실행
except:
    print("wrong input")
    sys.exit[1]


post = {"filename" : sys.argv[1]}
test_collection.insert_one(post)
print(test_collection.find())