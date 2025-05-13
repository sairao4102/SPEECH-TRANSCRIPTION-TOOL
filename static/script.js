// JavaScript code for handling audio file upload and recording

let mediaRecorder;  // Used to record audio
let audioChunks = [];  // Stores audio data while recording

// Upload selected audio file to the server
function uploadAudio() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  if (!file) return alert('Please select an audio file');

  const formData = new FormData();
  formData.append('audio_data', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert(data.error);
      return;
    }

    // Show the transcribed text
    showTranscript(data.transcript);

    // Play uploaded audio
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.src = URL.createObjectURL(file);
    audioPlayer.style.display = 'block';

    // Show and enable download button
    const downloadButton = document.getElementById('downloadLink');
    downloadButton.style.display = 'block';
    downloadButton.onclick = () => window.location.href = '/download';
  })
  .catch(err => alert('Error during upload or transcription: ' + err.message));
}

// Start recording from microphone
function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);
      audioChunks = [];

      // Collect audio data
      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };

      // When recording stops, upload and transcribe
      mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunks, { type: 'audio/wav' });
        const file = new File([blob], 'recorded.wav');

        const formData = new FormData();
        formData.append('audio_data', file);

        fetch('/upload', {
          method: 'POST',
          body: formData
        })
        .then(res => res.json())
        .then(data => {
          // Show transcript result
          showTranscript(data.transcript);

          // Play recorded audio
          const audioPlayer = document.getElementById('audioPlayer');
          audioPlayer.src = URL.createObjectURL(blob);
          audioPlayer.style.display = 'block';
        });

        // Hide recording indicator
        document.getElementById('recordingIndicator').style.display = 'none';
      };

      // Start recording
      mediaRecorder.start();
      document.getElementById('recordingIndicator').style.display = 'inline';
      alert('Recording started...');
    });
}

// Stop recording and send audio
function stopRecording() {
  if (mediaRecorder) {
    mediaRecorder.stop();
    alert('Recording stopped. Transcribing...');
  }
}

// Display the transcript text
function showTranscript(text) {
  document.getElementById('transcriptBox').style.display = 'block';
  document.getElementById('transcriptText').innerText = text;
}
