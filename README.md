# 🎙️ Jarvis Voice Assistant (Python)

A Python-based voice assistant built as a learning project to understand speech recognition, text-to-speech, API usage, and basic AI integration using Groq and other services.

This project focuses on clarity, simplicity, and learning, with well-commented code and a clean structure suitable for beginners.

✨ Features

🎤 Speech Recognition (voice → text)

🔊 Text-to-Speech responses

🎵 Play music using voice commands

🔗 Custom music library (song name → YouTube link)

🧠 AI-powered responses (API key required)

📝 Beginner-friendly and well-commented code

🧩 Modular file structure

🗂️ Project Structure

jarvis-voice-assistant/
│
├── main.py
├── client_test.py
├── musicLibrary.py
├── requirements.txt
├── LICENSE
└── README.md

🧠 How It Works (Simple Explanation)

The assistant listens to your voice using a microphone.

Speech is converted into text.

If the command matches a song name:

The assistant opens the mapped YouTube link.

Otherwise:

The command is sent to the AI model.

The response is spoken back using text-to-speech.

🎵 Music Library Explanation

The musicLibrary.py file contains a dictionary:

Key → Song name spoken by the user

Value → YouTube link of that song

Example:

music = {
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "enemy": "https://www.youtube.com/watch?v=e-xToC9wNl0",
    "pasoori": "https://www.youtube.com/watch?v=5Eqb_-j3FDA",
    "warriors": "https://www.youtube.com/watch?v=A7BYzjUvbWc"
}

▶️ Two Ways Music Is Played

1️⃣ Play from Music Library (Manual Mapping)
If the user says:

Play <song name>


The song name is searched as a key in musicLibrary.py

If found, the mapped YouTube link is opened and played

2️⃣ AI-Based Music Play (Dynamic Search)
If the user says:

Music <song name>

Example:

“Music Believer”

The command is sent to the AI model.

The AI returns a YouTube link

The assistant opens the link and plays the song

This allows:

Fast playback for favorite songs using the library

Flexible playback for any song using AI search

The assistant matches:
speech → text → song name → YouTube link → plays music

⚙️ Installation & Setup (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/HungerCoder01/jarvis-voice-assistant.git
cd jarvis-voice-assistant

2️⃣ (Recommended) Create a Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate


venv/ is intentionally not uploaded to GitHub (standard practice).

3️⃣ Install Required Modules
pip install -r requirements.txt

🔑 API Key Information (Important)

This repository does NOT include API keys.

You must add your own API keys.

Never push real API keys to GitHub.

Use placeholders like:

GROQ_API_KEY = "YOUR_API_KEY_HERE"

▶️ How to Run the Project
python main.py

Example Voice Commands:

“Jarvis” → Wake word

“Play Skyfall”

“Play Pasoori”

Ask general questions

“Stop” → Put assistant to sleep

📝 Notes & Best Practices

venv/ is not uploaded (safe and correct)

__pycache__/ is ignored

Extra comments are added intentionally for learning

Suitable for beginners and portfolio use

Clean and GitHub-ready structure

🙌 Learning & Credits

This project was built as a learning exercise inspired by tutorials and concepts from CodeWithHarry, then extended and implemented independently to improve understanding of Python, APIs, and AI integration.

📄 License

This project is licensed under the MIT License.

You are free to:

Use

Modify

Learn from

Share

⭐ Final Note

This is a learning-focused project, not a production assistant.
Clarity, comments, and simplicity are intentional.

Feel free to fork, improve, and experiment 🚀

✅ End of README
