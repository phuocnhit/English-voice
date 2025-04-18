const say = require('say');
const fs = require('fs');
const child_process = require('child_process');

const text = "Hello, this is a test of saving speech as an audio file.";
const outputFile = 'output.wav';

// Use the 'say' command to save speech as an audio file
const saveSpeechToFile = (text, outputFile) => {
  const command = `say -o ${outputFile} --data-format=LEF32@22050 "${text}"`;

  child_process.exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return;
    }
    console.log(`Audio saved as ${outputFile}`);
  });
};

saveSpeechToFile(text, outputFile);
