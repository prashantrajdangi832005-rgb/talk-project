import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Change voice if needed

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)   
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the recognition service.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I'm your Python voice assistant.")
    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that yet.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm ready.")
    while True:
        command = listen()
        if command:
            respond(command)
