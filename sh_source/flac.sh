name=`basename $1`
fileName="${name%.*}"  # 고유 이름
fileExtension="${name##*.}"  # 확장자

cd ~/capstone17_post/media
gsutil cp $1 gs://speech-ysh
rm $1
cd ~/stt
node stt.js $1 ${fileName}_overall.txt
cp ${fileName}_overall.txt ~/summary
cp ${fileName}_overall.txt ~/capstone17_post/capstone/static/capstone/overallview
rm ${fileName}_overall.txt
cd ~/summary
python3 summary.py ${fileName}_overall.txt $2 ${fileName}_summary.txt
rm ${fileName}_overall.txt 
cp output.txt ~/capstone17_post/capstone/static/capstone/summary
rm ${fileName}_summary.txt
