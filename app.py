import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import sys

# 1. Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Slightly faster, more natural speed
voices = engine.getProperty('voices')
# Index 0 is usually male, Index 1 is usually female (depends on OS)
engine.setProperty('voice', voices[0].id) 

def speak(text):
    """Converts text to audio output"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(recognizer, source):
    """Listens for audio and converts to text"""
    print("🎙️ Listening...")
    try:
        # timeout: how long to wait for speech
        # phrase_time_limit: max length of a sentence
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        # Only triggers if it hears noise but no recognizable words
        return ""
    except sr.RequestError:
        speak("I'm having trouble connecting to the internet.")
        return ""

def respond(command):
    """Logic for processing commands"""
    if "hello" in command:
        speak("Hi there! How can I help you?")

    elif "your name" in command:
        speak("I am your Python assistant. You can call me Py-Bot.")

    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "search for" in command:
        # Example: "search for space exploration"
        query = command.replace("search for", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "open" in command:
        # Example: "open youtube"
        site = command.replace("open", "").strip()
        speak(f"Opening {site}")
        webbrowser.open(f"https://www.{site}.com")

    elif "exit" in command or "bye" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        return False # This signals the loop to stop
    
    else:
        speak("I didn't quite get that, but I'm still learning!")
    
    return True # Keep the loop running

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        speak("System online. Calibrating for background noise...")
        # Calibrate once at start instead of every loop for speed
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("I am ready for your commands.")

        running = True
        while running:
            user_input = listen(recognizer, source)
            if user_input:
                running = respond(user_input)