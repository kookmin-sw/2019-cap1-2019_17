async function main() {
    // Imports the Google Cloud client library
    const speech = require('@google-cloud/speech');
    const fs = require('fs');
    var sf = require('sf');

    // Argument
    let inputArg = []
    process.argv.forEach(function (val, idx, array) {
        inputArg = array;
    });

    phrase = []

    fs.readFileSync('phrase.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
      phrase.push(line);
    })

    // Creates a client
    const client = new speech.SpeechClient();

    const audio = {
      //content: audioBytes,
      uri : `gs://speech-ysh/${inputArg[2]}`
    };
  
    const config = {
     enableWordTimeOffsets: true,       // 타임스탬프
     enableAutomaticPunctuation: true,  // 문단 띄어주는 기능.
     encoding: 'FLAC',
     languageCode: 'en-US',
     audioChannelCount: 2,
     useEnhanced: true,   // 데이터 로깅을 이용해 향상된 모델 사용
     "speechContexts": [{
     "phrases": phrase
      }]
    };
    const request = {
      audio: audio,
      config: config,
    };

    var database = {}
    database.table = []

   client
    .longRunningRecognize(request)
    .then(data => {
      const operation = data[0];
      
      // Get a Promise representation of the final result of the job
      return operation.promise();
    })
    .then(data => {
      const response = data[0];
      response.results.forEach(result => {

        var second = result.alternatives[0].words[0].startTime.seconds;
        var minute = parseInt(second / 60);
        var viewSecond = second % 60;
        var nanosecond = (result.alternatives[0].words[0].startTime.nanos)/100000000

        var timestamp = sf("{0:0#}:{1:0#}.{2:0#}", minute, viewSecond, nanosecond);
        var obj = {
            time: timestamp,
            transcript: `${result.alternatives[0].transcript}`,
        }
        database.table.push(obj);
        
        fs.writeFile (inputArg[4], JSON.stringify(database), function(err) {
          if (err) {
            console.error(err);
            return;
          };
        });
      });
      const transcription = response.results
        .map(result => result.alternatives[0].transcript)
        .join('.' + '\n');
      fs.writeFile(inputArg[3], transcription, 'utf8', function(err) {
        console.log(`${inputArg[3]} is created.`);
        console.log(`${inputArg[4]} is created.`);
      });
    })

  }
  main().catch(console.error);
