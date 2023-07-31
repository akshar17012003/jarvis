import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
    # print(voices[1].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=5:
        speak("Good morning!Today is a early start, Isnt it?")
    elif hour>=6 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Friday. How may i help you ??")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
        
    return query

if _name_ == "_main_":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching for the results....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'stackoverflow' in query:
            speak('Opening stackoverflow')
            webbrowser.open('stackoverflow.com')
        elif 'i love you' in query:
            speak('Sorry i am already booked')
            print('Sorry i am already booked')
        elif 'friday' in query:
            num=random.randint(0,4)
            if num==0:
                speak('Yes')
            elif num==1:
                speak('I am Available')
            elif num==2:
                speak('How may i assist you')
            elif num==3:
                speak('Yes!Go ahead i am listening')
            elif num==4:
                speak('Hi')
        elif 'Who are you' in query:
            speak('i am friday speed 1 terahetz memory 1 zetabyte')
        
        elif 'your version' in query:
            speak('version 1 point o')
        elif 'instagram' in query:
            speak('Opening instagram')
            webbrowser.open('instagram.com')
        elif 'mail' in query:
            speak('Opening gmail')
            webbrowser.open('gmail.com')
        elif 'cricket score' in query:
            speak("The live score")
            webbrowser.open('cricbuzz.com')
        elif 'amazon prime' in query:
            speak('Opening amazon prime')
            webbrowser.open('amazonprime.com')
        elif 'chatgpt' in query:
            speak('Opening my pear mate')
            webbrowser.open('chat.openai.com')
        elif 'news' in query:
            speak('Opening all news channels')
            webbrowser.open('tvhub.in')
        elif 'exit' or 'close' or 'quit' in query:
            speak('Closing.....')
            exit()