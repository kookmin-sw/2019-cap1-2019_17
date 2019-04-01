// Imports the Google Cloud client library
const speech = require('@google-cloud/speech');
let fs = require('fs');

// Creates a client
const client = new speech.SpeechClient();

/**
* TODO(developer): Uncomment the following lines before running the sample.
*/
const gcsUri = 'gs://capstone-project-2019/conana_show.wav';
const encoding = 'Eencoding of the audio file, e.g. LINEAR16';
const sampleRateHertz = 44100;
const languageCode = 'en-US';

const config = {
    encoding: encoding,
    sampleRateHertz: sampleRateHertz,
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
    fs.writeFile('output.txt', transcription, 'utf8', function(err) {
        console.log('asyn file output complete');
    });
})
.catch(err => {
    console.error('ERROR:', err);
});
