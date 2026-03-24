import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# --- CONFIG ---
SERP_API_KEY = "be875510650efbcae1c6c4ec70c972f502c871732d5302e8841fe7b16d3be46a"

engine = pyttsx3.init()
engine.setProperty('rate', 175)

# --- SPEAK FUNCTION ---
def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- SEARCH FUNCTION ---
def get_smart_answer(query):
    params = {
        "q": query,
        "location": "India",
        "hl": "en",
        "gl": "in",
        "google_domain": "google.com",
        "api_key": SERP_API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "answer_box" in results:
            return results["answer_box"].get("answer") or results["answer_box"].get("snippet")

        if "knowledge_graph" in results:
            return results["knowledge_graph"].get("description")

        if "organic_results" in results:
            return results["organic_results"][0].get("snippet")

        return "No answer found."

    except:
        return "Error connecting to search."

# --- VOICE INPUT ---
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_display("🎙️ Listening...\n")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except:
            return ""

# --- DISPLAY FUNCTION ---
def update_display(text):
    display.insert(tk.END, text)
    display.see(tk.END)

# --- MAIN RESPONSE ---
def process_command(command):
    update_display(f"\n🧑 You: {command}\n")

    if "time" in command:
        response = f"It's {datetime.now().strftime('%I:%M %p')}"

    elif command in ["exit", "bye", "quit"]:
        response = "Goodbye!"
        speak(response)
        update_display(f"🤖 Assistant: {response}\n")
        root.quit()
        return

    else:
        response = get_smart_answer(command)

    update_display(f"🤖 Assistant: {response}\n")
    speak(response)

# --- BUTTON ACTION ---
def on_click():
    command = entry.get().lower()
    entry.delete(0, tk.END)
    if command:
        process_command(command)

# --- VOICE BUTTON ---
def on_voice():
    command = listen()
    if command:
        process_command(command)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Voice Assistant (Display Mode)")
root.geometry("500x600")

display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)

btn_frame = tk.Frame(root)
btn_frame.pack()

send_btn = tk.Button(btn_frame, text="Send", command=on_click)
send_btn.pack(side=tk.LEFT, padx=5)

voice_btn = tk.Button(btn_frame, text="🎤 Speak", command=on_voice)
voice_btn.pack(side=tk.LEFT, padx=5)

# --- START ---
update_display("🤖 Assistant started...\n")
root.mainloop()