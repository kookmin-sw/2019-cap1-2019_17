cd ~/url
python3 url.py $1 $3
sudo rm immediate.flac
gsutil cp $3.flac gs://speech-ysh
sudo rm $3.flac
echo "flac cp"

cd ~/stt
export GOOGLE_APPLICATION_CREDENTIALS=key.json
node stt.js $3.flac $3_overall.txt $3_overall.json
echo "stt complete"
sudo cp $3_overall.txt ~/summary
sudo cp $3_overall.txt ~/capstone17_post/capstone/static/capstone/overallview
sudo cp $3_overall.json ~/capstone17_post/capstone/static/capstone/overallview
sudo rm $3_overall.txt
sudo rm $3_overall.json

cd ~/summary
python3 summary.py $3_overall.txt $2 $3_summary.txt $3_keyword.txt 
echo "summary complete"
sudo cp $3_summary.txt ~/capstone17_post/capstone/static/capstone/summary
echo "$3"
echo "summary cp complete"
sudo rm $3_overall.txt
echo "overall rm"
sudo rm $3_summary.txt
echo "summary rm"
sudo rm $3_keyword.txt
echo "keyword rm"
