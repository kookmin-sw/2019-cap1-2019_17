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
  
    // The name of the audio file to transcribe
    //const fileName = 'test/kks.flac';
  
    // Reads a local audio file and converts it to base64
    //const file = fs.readFileSync(fileName);
    //const audioBytes = file.toString('base64');
  
    // The audio file's encoding, sample rate in hertz, and BCP-47 language code LINEAR16
    // ko-KR, en-US
    const audio = {
      //content: audioBytes,
      uri : `gs://speech-ysh/${inputArg[2]}`
    };
  
    const config = {
     enableWordTimeOffsets: true,       // 타임스탬프
     enableAutomaticPunctuation: true,  // 문단 띄어주는 기능.
     encoding: 'FLAC',
  // sampleRateHertz: 44100,
     languageCode: 'en-US',
  // model: "default",
     audioChannelCount: 2,
     useEnhanced: true,   // 데이터 로깅을 이용해 향상된 모델 사용
  // enableSeparateRecognitionPerChannel: true,
  // LINEAR16, FLAC
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
        // console.log(`Transcription: ${result.alternatives[0].transcript}`);

        var second = result.alternatives[0].words[0].startTime.seconds;
        var minute = parseInt(second / 60);
        var viewSecond = second % 60;
        var nanosecond = (result.alternatives[0].words[0].startTime.nanos)/100000000
        //console.log(`${minute + `:` + viewSecond + `.` + nanosecond}`);

        var timestamp = sf("{0:0#}:{1:0#}.{2:0#}", minute, viewSecond, nanosecond);
        //console.log(`${timestamp}`);
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
          //console.log('complete');
        });
      });
      const transcription = response.results
        .map(result => result.alternatives[0].transcript)
        .join('\n');
      fs.writeFile(inputArg[3], transcription, 'utf8', function(err) {
        console.log(`${inputArg[3]} is created.`);
        console.log(`${inputArg[4]} is created.`);
      });
    })

  }
  main().catch(console.error);
