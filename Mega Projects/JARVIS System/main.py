import speech_recognition as sr
import pyttsx3
import logging
import os
from datetime import datetime as dt
import webbrowser
import wikipedia as wiki

# This is logger for the application
def log_info(error):
    # Path Initialization
    DIR_LOC = "Logs"
    DIR_FILE = "Application.log"
    os.makedirs(DIR_LOC, exist_ok=True)
    path = os.path.join(DIR_LOC, DIR_FILE)

    # Configure logging
    logging.basicConfig(
        filename=path,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-%Y %I:%M:%S %p",
        level=logging.INFO
    )

    # Log a message
    logging.info(error)


def speak(text):
    """
    This function converts text to a voice
    
    Args: text
    return: voice
    """

    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set the desired voice based on gender
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    
    # Speak a sample text
    engine.say(text)
    engine.runAndWait()

    print(text)
    

def takeCommand():
    """
    This function takes command & recognize

    return: query
    """

    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        # record audio
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        # Recognize speech using Google Web Speech API
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        log_info(e)
        unknown = "Sorry! I don't understand"
        return unknown
    
    return query

# This function will wish you
def wish_me():
    hour = dt.now().hour
    if 5 <= hour < 12:
        speak("Good Morning Boss! How are you doing")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss! How are you doing")
    else:
        speak("Good Evening Boss! How are you doing")

    speak("I am JARVIS. Tell me Boss. How can i help you?")

wish_me()
while True:
    text = takeCommand().lower()
    if any(word in text for word in ["shutdown", "exit"]):
        speak("Good Bye Boss!")
        exit()
    
    elif "time" in text:
        speak(dt.now().strftime("%I:%M %p"))
    
    elif "name" in text:
        speak("My name is JARVIS")

    elif "google" in text:
        speak("Ok Boss.")
        webbrowser.open("google.com")

    elif "github" in text:
        speak("Ok Boss.")
        webbrowser.open("github.com")

    elif "youtube" in text:
        speak("Ok Boss.")
        webbrowser.open("youtube.com")

    # This query for search something from wikipedia
    elif "wikipedia" in text:
        speak("Searching wikipedia")
        text = text.replace("wikipedia", "")
        results = wiki.summary(text, sentences=2)
        speak("According to wikipedia " + text)
        speak(results) 
    
    else:
        speak(text)

