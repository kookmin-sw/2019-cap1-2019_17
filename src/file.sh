name=`basename $1`
fileName="${name%.*}"  # 고유 이름
fileExtension="${name##*.}"  # 확장자
           
cd ~/capstone17/media
sudo python3 getDuration.py $1
sudo cp ${fileName}_duration.txt ~/db
sudo rm ${fileName}_duration.txt
gsutil cp $1 gs://speech-ysh
echo "flac cp"

cd ~/stt
export GOOGLE_APPLICATION_CREDENTIALS=key.json
node stt.js $1 ${fileName}_overall.txt ${fileName}_overall.json
echo "stt complete"
sudo cp ${fileName}_overall.txt ~/summary
sudo cp ${fileName}_overall.txt ~/capstone17/capstone/static/capstone/overallview
sudo cp ${fileName}_overall.json ~/capstone17/capstone/static/capstone/overallview
sudo rm ${fileName}_overall.txt
sudo rm ${fileName}_overall.json

cd ~/summary
echo "summary cd"
python3 summary.py ${fileName}_overall.txt $2 ${fileName}_summary.txt ${fileName}_keyword.txt 
echo "summary complete"
sudo cp ${fileName}_summary.txt ~/capstone17/capstone/static/capstone/summary
echo "${fileName}"
echo "summary cp complete"
sudo rm ${fileName}_overall.txt
echo "overall rm"
sudo rm ${fileName}_summary.txt
echo "summary rm"
sudo cp ${fileName}_keyword.txt ~/db
sudo rm ${fileName}_keyword.txt
echo "keyword rm"

cd ~/db
python3 dataToDB.py ${fileName}
sudo rm ${fileName}_duration.txt
sudo rm ${fileName}_keyword.txt
echo "mongodb complete"