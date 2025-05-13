# Speech Transcription Tool

This is a **Speech Transcription Tool** developed to transcribe audio files into text using speech recognition. The tool supports various audio formats such as WAV, MP3, FLAC, and AIFF, and provides a simple interface for uploading and transcribing audio files. It also allows real-time recording through the browser and transcribes the recorded audio.

## Features

- **Upload Audio File**: Upload any supported audio file (WAV, MP3, FLAC, AIFF) and get the transcription.
- **Real-time Recording**: Record audio through the browser using the microphone and transcribe it in real-time.
- **Audio Playback**: Play back the uploaded or recorded audio along with the transcribed text.
- **Download Transcript**: Download the transcript as a text file after transcription.
- **Supports Multiple Formats**: Handles WAV, MP3, FLAC, and AIFF audio formats.

## Technologies Used

- **SpeechRecognition**: For transcribing the audio into text using Google Web Speech API.
- **Flask**: A lightweight web framework for building the backend of the application.
- **JavaScript**: For client-side interaction (e.g., uploading files, recording audio).
- **HTML/CSS**: For creating the web interface.
- **Pydub**: For handling audio file conversions (e.g., MP3 to WAV).

## How It Works

1. **Upload Audio**: Users can upload audio files through the web interface. The backend converts the audio into a format that can be processed and transcribed.
2. **Transcription**: The audio is transcribed into text using the Google Web Speech API, and the text is returned to the user.
3. **Download Option**: After transcription, the user can download the transcript as a text file.
4. **Real-Time Recording**: Users can also record their own audio directly through the browser and get it transcribed.

