# Jarvis Voice Assistant
# A Python-based voice assistant built while learning Python,
# speech recognition, text-to-speech, APIs, and AI integration.

# Features:
# - Wake word detection ("Jarvis")
# - Voice-controlled web actions
# - AI-powered responses using Groq
# - Music playback via YouTube links
# - News headlines reader
# - Custom "stop" sleep command


# NOTE:
# Replace the placeholder API keys with your own before running the project

# Import required libraries for speech recognition, text-to-speech,
# web browsing, AI integration, and media playback


import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary 
import requests
from groq import Groq
from gtts import gTTS
# from google import genai  # Planned for future AI experiments
import pygame 
import time
import os

# NOTE:
# If you are using the Code Runner extension in VS Code, disable it.
# It may run the code using the global Python interpreter instead of the virtual environment (venv),
# which can cause microphone, audio, and dependency-related issues in this project.

# Creates a speech recognizer object that converts spoken audio into text
recognizer = sr.Recognizer()

# Store News API key (replace with your own key)
newsapi = "News_API_Key"


# NOTE:
# This approach caused issues where the speak() function stopped working
# after the first execution, so it is not used in this project.
# engine = pyttsx3.init

# def speak(text): 
#     engine.say(text)
#     engine.runAndWait()  


# NOTE:
# Use only one text-to-speech method at a time.
# Using pyttsx3 and gTTS together may cause audio and playback issues.

# Text-to-Speech using pyttsx3 
# The engine is initialized each time to prevent audio device lock issues
# def speak(text):

#     # "sapi5" is Windows-specific
#     engine = pyttsx3.init("sapi5")   # reattach to audio device
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()


# Using Google Cloud Text-to-Speech (paid service)
# It works only for a short free duration but is included to understand how it works

def speak(text):
    tts = gTTS(text) 
    tts.save("temp.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load MP3 file
    pygame.mixer.music.load("temp.mp3")  # put mp3 in same folder or give full path

    # Play the music
    pygame.mixer.music.play()

    # Keep program running while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# This function sends user commands to the Groq AI model
# and returns the AI-generated response
def aiProcess(command):
    client = Groq(api_key="Groq_API_Key")

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            # {"role": "system", "content": "You are Jarvis, a helpful assistant. Give short responses"},
            
            # System prompt is customized so that:
            # - If the user asks for music, AI responds ONLY with a YouTube link
            # - Otherwise, AI behaves like a normal assistant
            
            {"role": "system", "content":"""You are Jarvis, a voice-based AI assistant.

                                        CRITICAL RULES (DO NOT BREAK):

                                        1. MUSIC COMMAND:
                                        - If the user input starts with the word "music":
                                            Example: "music shape of you"
                                        - Respond ONLY in this format:
                                        https://youtube.com/watch?v=VIDEO_ID
                                        - Provide ONLY ONE YouTube link.
                                        - The link MUST be a commonly known, playable video.
                                        - Do NOT add extra words, symbols, emojis, or explanations.
                                        - If a playable link cannot be guaranteed, respond exactly:
                                            Sorry, I could not find a playable link for that song.

                                        2. NORMAL COMMANDS (Non-music):
                                        - Respond in short, clean sentences.
                                        - NO markdown, NO bullet points, NO symbols (* # - _).
                                        - NO emojis.
                                        - Keep the reply under 1-3 sentences unless the user asks for detail.
                                        - Text must be clean for text-to-speech.

                                        3. FORMATTING RULES (VERY IMPORTANT):
                                        - Plain text only.
                                        - No special characters.
                                        - No code blocks.
                                        - No lists.
                                        - No extra spacing.

                                        You are optimized for voice output. Clarity and simplicity are mandatory."""
            },
            
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message.content


# This function handles all user commands
# It matches spoken commands with predefined actions
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        # If command is like "play songname":
        # - Split the command
        # - Extract the song name
        # - Fetch the corresponding YouTube link from musicLibrary

        song = c.lower().split(" ")[1] 

        # Assumes the song exists in the musicLibrary dictionary

        link = musicLibrary.music[song] # musicLibrary.py contains a dictionary created by me
                                        # that maps song names to their corresponding YouTube links 
        speak(f"Playing {song} song")
        webbrowser.open(link)
    elif "news" in c.lower(): # Fetch top news headlines using News API
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:

            # Parse the JSON response
            data = r.json()

            # Extract the list of news articles
            articles = data.get('articles',[])

            # Speak out each news headline
            for article in articles:
                speak(article['title'])
    else:
        # If command does not match predefined actions,
        # let the AI handle the request
        
        output = aiProcess(c)
        # speak(output)

        # This logic is designed by me:
        # If AI returns a YouTube link, it plays the song
        # Otherwise, it speaks the AI response normally 
        if("https://www.youtube.com" in output):
            speak("Playing A Song")
            webbrowser.open(output)
        else:
            speak(output)
           
# Entry point of the program
if __name__ == "__main__":
    # Initialize Jarvis voice assistant
    speak("Initializing Jarvis....") 

    work = True

    while work:
        # Listen continuously for the wake word "Jarvis"
        r = sr.Recognizer()
        

        # IMPORTANT:
        # Do NOT use PocketSphinx here.
        # It does not recognize words clearly.
        # Google Speech Recognizer gives much better accuracy.
        
        # # recognize speech using Sphinx
        # try:
        #     command = r.recognize_sphinx(audio)
        #     print(command)
        #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:
        #     print("Sphinx error; {0}".format(e))

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                
                print("Listening...")
                audio = r.listen(source ,timeout = 2,phrase_time_limit = 1) 
           
            word = r.recognize_google(audio)
            
           
            if(word.lower() == "stop"):
                # Custom feature added by me:
                # Saying "stop" puts Jarvis into sleep mode
                speak("Jarvis is now going to sleep mode")
                work = False

            if (word.lower() == "jarvis"):
                # When wake word "Jarvis" is detected,
                # activate the assistant and listen for commands

                speak("YA")
               
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source) 
                    command = r.recognize_google(audio)
                    print(f"Given Command: {command}\n")
                    processCommand(command)

                    

            # print(command)

        # Handle microphone, speech recognition, or runtime errors safely   
        except Exception as e:
            print("Error; {0}".format(e))


