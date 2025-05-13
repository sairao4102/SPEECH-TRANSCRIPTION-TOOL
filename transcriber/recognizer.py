# This script uses the SpeechRecognition library to transcribe audio files.
# It supports various audio formats and converts them to WAV format if necessary.

# Importing necessary libraries
import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile

def transcribe_audio(audio_path):
    # Creating a recognizer object to process the audio
    recognizer = sr.Recognizer()

    # Convert to WAV (PCM) if not already
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        try:
            # Convert any format to WAV using pydub
            audio = AudioSegment.from_file(audio_path)
            audio.export(temp_wav.name, format="wav")
            temp_wav_path = temp_wav.name
        except Exception as e:
            return f"Audio conversion failed: {str(e)}"
   #Use Google’s API to recognize and convert speech to text
    try:
        with sr.AudioFile(temp_wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text
    except Exception as e:
        return f"Transcription failed: {str(e)}"
    finally:
        os.remove(temp_wav_path)
