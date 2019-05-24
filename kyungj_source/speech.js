let inputArg = []
process.argv.forEach(function (val, idx, array) {
  inputArg = array;
});

// Imports the Google Cloud client library
const speech = require('@google-cloud/speech');
let fs = require('fs');

// Creates a client
const client = new speech.SpeechClient();

/**
* TODO(developer): Uncomment the following lines before running the sample.
*/
const gcsUri = `gs://capstone-project-2019/${inputArg[2]}`;
const encoding = 'FLAC';
// const sampleRateHertz = 16000;
const languageCode = 'en-US';
const audioChannelCount = 2;

const config = {
    encoding: encoding,
    audioChannelCount: audioChannelCount,
    languageCode: languageCode,
    enableWordTimeOffsets: true,
    enableAutomaticPunctuation: true,
};

const audio = {
    uri: gcsUri,
};

const request = {
    config: config,
    audio: audio,
};

// Detects speech in the audio file. This creates a recognition job that you
// can wait for now, or get its result later.
client
.longRunningRecognize(request)
.then(data => {
    const operation = data[0];
    // Get a Promise representation of the final result of the job
    return operation.promise();
})
.then(data => {
    const response = data[0];
    const transcription = response.results
    .map(result => result.alternatives[0].transcript)
    .join('\n');
    //console.log(`Transcription: ${transcription}`);
    fs.writeFile(inputArg[3], transcription, 'utf8', function(err) {
        console.log(`${inputArg[3]} is created.`);
    });
})
.catch(err => {
    console.error('ERROR:', err);
});