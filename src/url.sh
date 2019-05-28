cd ~/capstone17/media
python3 url.py \"$1\" $3
echo "get flac"
sudo rm immediate.flac
sudo python3 getDuration.py $3.flac
sudo cp $3_duration.txt ~/db
sudo rm $3_duration.txt
gsutil cp $3.flac gs://speech-ysh
echo "flac cp"

cd ~/stt
export GOOGLE_APPLICATION_CREDENTIALS=key.json
node stt.js $3.flac $3_overall.txt $3_overall.json
echo "stt complete"
sudo cp $3_overall.txt ~/summary
sudo cp $3_overall.txt ~/capstone17/capstone/static/capstone/overallview
sudo cp $3_overall.json ~/capstone17/capstone/static/capstone/overallview
sudo rm $3_overall.txt
sudo rm $3_overall.json

cd ~/summary
python3 summary.py $3_overall.txt $2 $3_summary.txt $3_keyword.txt 
echo "summary complete"
sudo cp $3_summary.txt ~/capstone17/capstone/static/capstone/summary
echo "$3"
echo "summary cp complete"
sudo rm $3_overall.txt
echo "overall rm"
sudo rm $3_summary.txt
echo "summary rm"
sudo cp $3_keyword.txt ~/db
sudo rm $3_keyword.txt
echo "keyword rm"

cd ~/db
python3 dataToDB.py $3
sudo rm $3_duration.txt
sudo rm $3_keyword.txt
echo "mongodb complete"