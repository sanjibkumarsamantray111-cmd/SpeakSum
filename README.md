## SpeakSum

SpeakSum is a voice-controlled calculator that performs real-time addition using speech recognition.  
It allows users to input numbers by speaking, making calculations hands-free and efficient.

---

## Features

- 🎙️ Speech-to-Text number recognition
- ➕ Automatic addition (default operation)
- 📊 Real-time expression building
- 🔢 Direct digit recognition (no word parsing required)
- ⚡ Fast and lightweight Python implementation

---

## Tech Stack

- Python 3.11
- SpeechRecognition
- Google Speech API
- Git & GitHub

---

## 📂 Project Structure

SpeakSum/
│
├── calculator_core.py # Core calculation logic
├── mic_test.py # Microphone testing script
├── test.py # Core logic testing
└── voice_calculator.py # Main voice calculator loop


---

▶ How to Run

1. Clone the repository:

```bash
git clone https://github.com/sanjibkumarsamantray111-cmd/SpeakSum.git
cd SpeakSum

# Install all Dependencies

pip install SpeechRecognition pyaudio

## Run the Voice Calculator

python voice_calculator.py
