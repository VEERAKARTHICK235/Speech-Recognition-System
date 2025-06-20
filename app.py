from flask import Flask, render_template, request, jsonify, send_file
import speech_recognition as sr
from pydub import AudioSegment
import os, tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def transcribe_file(file_stream):
    # Validate supported file types
    if not file_stream.filename.endswith(('.wav', '.mp3', '.flac', '.ogg', '.m4a')):
        raise ValueError("Unsupported audio format. Please upload .wav, .mp3, .flac, .ogg or .m4a")

    # Convert uploaded audio to standard format for recognition
    audio = AudioSegment.from_file(file_stream)
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        audio.set_channels(1).set_frame_rate(16000).export(tmp.name, format='wav')
        temp_path = tmp.name

    recog = sr.Recognizer()
    with sr.AudioFile(temp_path) as src:
        data = recog.record(src)
        text = recog.recognize_google(data, language='en-US')  # Default to English

    os.unlink(temp_path)
    return text

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify(err="No file"), 400
    try:
        text = transcribe_file(request.files['file'])
        return jsonify(text=text)
    except Exception as e:
        return jsonify(err=str(e)), 500

@app.route('/record', methods=['POST'])
def record():
    if 'audio' not in request.files:
        return jsonify(err="No audio"), 400
    try:
        text = transcribe_file(request.files['audio'])
        return jsonify(text=text)
    except Exception as e:
        return jsonify(err=str(e)), 500

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    text = request.form.get('text', '')
    buf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(buf.name, pagesize=A4)
    width, height = A4
    margin = 50
    max_width = width - 2 * margin
    font_size = 12
    line_height = font_size * 1.2

    c.setFont("Times-Roman", font_size)

    lines = []
    for paragraph in text.split('\n'):
        wrapped_lines = simpleSplit(paragraph, "Times-Roman", font_size, max_width)
        lines.extend(wrapped_lines)
        lines.append('')

    y = height - margin
    for line in lines:
        if y < margin:
            c.showPage()
            c.setFont("Times-Roman", font_size)
            y = height - margin
        c.drawString(margin, y, line)
        y -= line_height

    c.save()
    return send_file(buf.name, as_attachment=True, download_name="transcript.pdf")

if __name__ == "__main__":
    app.run(debug=True)
