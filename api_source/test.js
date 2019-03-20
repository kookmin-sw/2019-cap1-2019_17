
//
// node js 프롬프트로 해야함
//desktop에서 set GOOGLE_APPLICATION_CREDENTIALS=key.json
// set은 종료시마다 계속적으로 해줘야함. ubuntu는 export
//async function quickstart(
//  projectId = 'certain-armor-233710', // Your Google Cloud Platform project ID
//  bucketName = 'my-new-bucket' // The name for the new bucket
//) {
//  // Imports the Google Cloud client library
//  const {Storage} = require('@google-cloud/storage');
//
//  // Creates a client
//  const storage = new Storage({projectId});
//
//  // Creates the new bucket
//  await storage.createBucket(bucketName);
//  console.log(`Bucket ${bucketName} created.`);
//}

async function main(){
  // Imports the Google Cloud client library
  const speech = require('@google-cloud/speech');
  //const fs = require('fs');

  // Creates a client
  const client = new speech.SpeechClient();

  // The name of the audio file to transcribe
  //const fileName = 'test/yw.flac';
  
  // Reads a local audio file and converts it to base64
  //const file = fs.readFileSync(fileName);
  //const audioBytes = file.toString('base64');
  
  // The audio file's encoding, sample rate in hertz, and BCP-47 language code LINEAR16
  // ko-KR, en-US
  const audio = {
    uri: 'gs://speech-ysh/MS.flac'
  };
  const config = {
//	enableWordTimeOffsets: true,
	enableAutomaticPunctuation: true,
//  encoding: 'LINEAR16',
	encoding: 'FLAC',
	sampleRate: 16000,
    languageCode: 'en-US',
//	languageCode: 'ko-KR',
//	model: "default",
	audioChannelCount: 2,
//  enableSeparateRecognitionPerChannel: true,
// LINEAR16, FLAC
  };
  const request = {
    audio: audio,
    config: config,
  };

 client
  .longRunningRecognize(request)
  .then(data => {
    const operation = data[0];
    
    return operation.promise();
  })
  .then(data => {
    const response = data[0];
    response.results.forEach(result => {
      console.log(`Transcription: ${result.alternatives[0].transcript}`);
      result.alternatives[0].words.forEach(wordInfo => {
        const startSecs =
          `${wordInfo.startTime.seconds}` +
          `.` +
          wordInfo.startTime.nanos / 100000000;
        const endSecs =
          `${wordInfo.endTime.seconds}` +
          `.` +
          wordInfo.endTime.nanos / 100000000;
        console.log(`Word: ${wordInfo.word}`);
        console.log(`\t ${startSecs} secs - ${endSecs} secs`);
      });
    });
  })

	
}
main().catch(console.error);

/**
 * Copyright 2017, Google, Inc.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * This application demonstrates how to perform basic recognize operations with
 * with the Google Cloud Speech API.
 *
 * For more information, see the README.md under /speech and the documentation
 * at https://cloud.google.com/speech/docs.
 */
//
//'use strict';
//
///**
// * Note: Correct microphone settings is required: check enclosed link, and make
// * sure the following conditions are met:
// * 1. SoX must be installed and available in your $PATH- it can be found here:
// * http://sox.sourceforge.net/
// * 2. Microphone must be working
// * 3. Encoding, sampleRateHertz, and # of channels must match header of audio file you're
// * recording to.
// * 4. Get Node-Record-lpcm16 https://www.npmjs.com/package/node-record-lpcm16
// * More Info: https://cloud.google.com/speech-to-text/docs/streaming-recognize
// */
//
//// const encoding = 'LINEAR16';
//// const sampleRateHertz = 16000;
//// const languageCode = 'en-US';
//
//function microphoneStream(encoding, sampleRateHertz, languageCode) {
//  // [START micStreamRecognize]
//
//  // Node-Record-lpcm16
//  const record = require('node-record-lpcm16');
//
//  // Imports the Google Cloud client library
//  const speech = require('@google-cloud/speech');
//
//  const config = {
//    encoding: encoding,
//    sampleRateHertz: sampleRateHertz,
//    languageCode: languageCode,
//  };
//
//  const request = {
//    config,
//    interimResults: false, //Get interim results from stream
//  };
//
//  // Creates a client
//  const client = new speech.SpeechClient();
//
//  // Create a recognize stream
//  const recognizeStream = client
//    .streamingRecognize(request)
//    .on('error', console.error)
//    .on('data', data =>
//      process.stdout.write(
//        data.results[0] && data.results[0].alternatives[0]
//          ? `Transcription: ${data.results[0].alternatives[0].transcript}\n`
//          : `\n\nReached transcription time limit, press Ctrl+C\n`
//      )
//    );
//
//  // Start recording and send the microphone input to the Speech API
//  record
//    .start({
//      sampleRateHertz: sampleRateHertz,
//      threshold: 0, //silence threshold
//      recordProgram: 'rec', // Try also "arecord" or "sox"
//      silence: '5.0', //seconds of silence before ending
//    })
//    .on('error', console.error)
//    .pipe(recognizeStream);
//
//  console.log('Listening, press Ctrl+C to stop.');
//  // [END micStreamRecognize]
//}
//
//require(`yargs`)
//  .demand(1)
//  .command(
//    `micStreamRecognize`,
//    `Streams audio input from microphone, translates to text`,
//    {},
//    opts =>
//      microphoneStream(opts.encoding, opts.sampleRateHertz, opts.languageCode)
//  )
//  .options({
//    encoding: {
//      alias: 'e',
//      default: 'LINEAR16',
//      global: true,
//      requiresArg: true,
//      type: 'string',
//    },
//    sampleRateHertz: {
//      alias: 'r',
//      default: 16000,
//      global: true,
//      requiresArg: true,
//      type: 'number',
//    },
//    languageCode: {
//      alias: 'l',
//      default: 'en-US',
//      global: true,
//      requiresArg: true,
//      type: 'string',
//    },
//  })
//  .example(`node $0 micStreamRecognize`)
//  .wrap(120)
////  .recommendCommands()
//  .epilogue(`For more information, see https://cloud.google.com/speech/docs`)
//  .help()
//  .strict().argv;