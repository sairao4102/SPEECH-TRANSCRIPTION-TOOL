# This code is a simple Flask web application that allows users to upload audio files for transcription.

from flask import Flask, render_template, request, send_file, jsonify
import os
from transcriber.recognizer import transcribe_audio  # Importing the audio transcription function from recognizer.py

app = Flask(__name__)

# Folders to store uploaded audio and saved transcripts
UPLOAD_FOLDER = 'uploads'
TRANSCRIPT_FOLDER = 'transcripts'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPT_FOLDER, exist_ok=True)

# Supported audio formats
ALLOWED_EXTENSIONS = {'wav', 'flac', 'mp3', 'aiff'}

# Check if file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle audio upload and transcription
@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    audio_file = request.files['audio_data']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(audio_file.filename):
        return jsonify({'error': 'Invalid file format. Only WAV, FLAC, MP3, and AIFF are allowed.'}), 400

    # Save uploaded audio file
    filename = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(filename)

    try:
        # Get transcript from audio
        transcript = transcribe_audio(filename)

        # Save transcript as a text file
        transcript_filename = os.path.join(TRANSCRIPT_FOLDER, f'{os.path.splitext(audio_file.filename)[0]}.txt')
        with open(transcript_filename, 'w', encoding='utf-8') as f:
            f.write(transcript)

        return jsonify({'transcript': transcript})
    except Exception as e:
        return jsonify({'error': f'An error occurred during transcription: {str(e)}'}), 500

# Route to download the transcript file
@app.route('/download/<filename>')
def download_transcript(filename):
    transcript_path = os.path.join(TRANSCRIPT_FOLDER, filename)
    if os.path.exists(transcript_path):
        return send_file(transcript_path, as_attachment=True)
    else:
        return jsonify({'error': 'Transcript not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
