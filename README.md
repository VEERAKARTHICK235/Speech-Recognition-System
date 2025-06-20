# Speech-Recognition-System

This project implements two different speech-to-text systems:
1. Using Google's Speech Recognition API via the SpeechRecognition library
2. Using Facebook's Wav2Vec model

## Requirements

- Python 3.7+
- The required packages listed in `requirements.txt`

## Installation

1. Clone this repository
2. Install the requirements:# 🎙️ Speech Recognition System

A Flask web app that converts speech (uploaded or recorded) into text using `SpeechRecognition` and Google API. It supports multiple languages and allows users to **download the transcript as a PDF**.

> 🌐 [Live Demo](https://speech-recognition-system-srs.onrender.com/)  


---

## 🚀 Features

- 🔊 Upload or record audio in `.mp3`, `.wav`, `.flac`, `.ogg`, or `.m4a`
- 📄 Export transcribed text as a PDF
- ⚡ Clean, modern UI with a glowing futuristic design
- 🔐 Input validation & error handling

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Libraries:**  
  - `SpeechRecognition`  
  - `Pydub`  
  - `ReportLab`  
  - `FFmpeg` (required for audio conversion)

---

## 📦 Installation

### 1. Clone this repo

```bash
git clone https://github.com/VEERAKARTHICK235/speech-recognition-system.git
cd speech-recognition-system

   ```bash
   pip install -r requirements.txt
