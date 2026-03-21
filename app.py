import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch
from datetime import datetime


# # --- CONFIGURATION ---
# SERP_API_KEY = "be875510650efbcae1c6c4ec70c972f502c871732d5302e8841fe7b16d3be46a" # <--- Put your key here

# engine = pyttsx3.init()
# engine.setProperty('rate', 175)

# def speak(text):
#     print(f"Assistant: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def get_smart_answer(query):
#     """Uses SerpApi to get the actual direct answer from Google."""
#     params = {
#         "q": query,
#         "location": "United States",
#         "hl": "en",
#         "gl": "us",
#         "google_domain": "google.com",
#         "api_key": SERP_API_KEY
#     }
    
#     try:
#         search = GoogleSearch(params)
#         results = search.get_dict()
        
#         # 1. Try to find an "Answer Box" (Direct result)
#         if "answer_box" in results:
#             box = results["answer_box"]
#             if "answer" in box: return box["answer"]
#             if "snippet" in box: return box["snippet"]
            
#         # 2. Try to find "Knowledge Graph" (Facts)
#         if "knowledge_graph" in results:
#             return results["knowledge_graph"].get("description")
            
#         # 3. Fallback to the first organic snippet
#         if "organic_results" in results:
#             return results["organic_results"][0].get("snippet")
            
#         return "I found some info, but no direct answer. Try rephrasing."
#     except Exception as e:
#         return "I had trouble reaching the search servers."

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎙️ Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
#             command = recognizer.recognize_google(audio)
#             print(f"You said: {command}")
#             return command.lower()
#         except:
#             return ""

# def respond(command):
#     # Standard commands
#     if "time" in command:
#         speak(f"It's {datetime.now().strftime('%I:%M %p')}")
    
#     elif "exit" in command or "bye" in command:
#         speak("Goodbye!")
#         return False

#     # Smart Search commands (Any question starting with 'who', 'what', 'where', 'how')
#     elif any(word in command for word in ["who", "what", "where", "how", "tell me"]):
#         speak("Let me check that for you...")
#         answer = get_smart_answer(command)
#         speak(answer)
    
#     else:
#         speak("I'm listening. Ask me a question like 'Who is the president?'")
    
#     return True

# if __name__ == "__main__":
#     speak("Voice system active.")
#     running = True
#     while running:
#         user_input = listen()
#         if user_input:
#             running = respond(user_input)