name=`basename $1`
fileName="${name%.*}"  # 고유 이름
fileExtension="${name##*.}"  # 확장자
           
cd ~/capstone17_post/media
gsutil cp $1 gs://speech-ysh
sudo rm $1
cd ~/stt
export GOOGLE_APPLICATION_CREDENTIALS=key.json
node stt.js $1 ${fileName}_overall.txt ${fileName}_overall.json
echo "stt complete"
sudo cp ${fileName}_overall.txt ~/summary
sudo cp ${fileName}_overall.txt ~/capstone17_post/capstone/static/capstone/overallview
sudo cp ${fileName}_overall.json ~/capstone17_post/capstone/static/capstone/overallview
sudo rm ${fileName}_overall.txt
sudo rm ${fileName}_overall.json
cd ~/summary
echo "summary cd"
python3 summary.py ${fileName}_overall.txt $2 ${fileName}_summary.txt ${fileName}_keyword.txt 
echo "summary complete"

sudo cp ${fileName}_summary.txt ~/capstone17_post/capstone/static/capstone/summary
echo "${fileName}"
echo "summary cp complete"
sudo rm ${fileName}_overall.txt
echo "overall rm"
sudo rm ${fileName}_summary.txt
echo "summary rm"
sudo rm ${fileName}_keyword.txt
echo "keyword rm"
