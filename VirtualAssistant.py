import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


myName = "FireBrigate"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak("Good Morning, Have a great day.")
    elif hour>12 and hour<18:
        speak("Good Afternoon, Have a great noon.")
    else:
        speak("Good Evening, Have a great evening.")
    speak(f'I am {myName}, How may I help you?')


def hearMe():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print('You Said:',query)
    except Exception:
        print("Please, say again")
        return 'None'
    return query
    

if __name__ == "__main__":
    wishme()
    while True:
        query = hearMe().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        
        else:
            search = 'https://www.google.com/search?q='+query
            webbrowser.open(search)
        


 