import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
 import openai

 def ai(query):
     openai.api_key = ''
     text = f"Artificial Intelligence response of Question: {query}\n**********\n\n"
     response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         prompt=query,
         temperature=0.7,
         max_tokens=1000,
         top_p=1.0,
         frequency_penalty=0,
         presence_penalty=0
     )
     text += response['choices'][0]['message']['content']

     if not os.path.exists("Aiopen"):
         os.mkdir("Aiopen")

     with open(f"#define the path for a folder to save the document{random.randint(1, 789622354785)}.txt",
               "w") as f:
         f.write(text)

     return text

def say(text):
    engine = pyttsx3.init()

    for voice in engine.getProperty('voices'):
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()

def get_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("You:", end=" ")
        audio = recognizer.listen(source)

    try:
        user_response = recognizer.recognize_google(audio)
        print(user_response)
        return user_response
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""

def main():
    say('Are you Fardeen')
    user_response = get_user_input()

    if "your boss".lower() in user_response.lower():
        print('Initializing')
        say('Hello Fardeen, I am Stew. You can call me Jarvis.')
        say('Can I do anything for you?')
        print("Analyzing...")
        while True:
            query = get_user_input()
            if "terminate" in query.lower():
                say('Hope I will see you soon again')
                exit()

             if "artificial intelligence" in query.lower():
                 response_text = ai(query)
                 say(response_text)

            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                     ["google", "https://www.google.com"], ["Instagram", "https://www.instagram.com"]]

            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say('Opening the site you requested')
                    webbrowser.open(site[1])

            if "open music" in query.lower():
                path_music = "" #define the music folder path
                os.startfile(path_music)

            if "the time" in query.lower():
                timenow = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The time now is {timenow}")

            if "open code" in query.lower():
                path_code = r"" #define the path here VsCode
                os.startfile(path_code)

            if "any update".lower() in query.lower():
                webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')

    else:
        say('Access denied')

if __name__ == "__main__":
    main()
