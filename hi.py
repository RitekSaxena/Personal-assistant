import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search
import google


# Put your Chrome application's path here
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# initializing the voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# setting the voice
engine.setProperty('voice', voices[len(voices)-2].id)


# takes a string and pronounce it
def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('good morning,sir!')

    if currentH >= 12 and currentH < 18:
        speak('good afternoon,Sir!')

    if currentH >= 18 and currentH != 0:
        speak('good evening,Sir!')

    speak(" I am your assistant , how may I help you?")

# Take your voice command


def takeCommand():
    r = sr.Recognizer()

    # put your microphone's index as the argument to sr.Microphone function.
    # You can get indexes of connected microphones by running audio.py file
    with sr.Microphone(1) as source:
        print("Listening...")
        # 0.6 sec pause in your voice will breake the listening process and it will start recognizing
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("recognizing...")
        # Google speech recognizer
        query = r.recognize_google(audio, language='en-in')
        print('User said : ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


greetMe()

while True:

    query = takeCommand().lower()

# Implemeted function to do various tasks.

    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("opening google")
        webbrowser.open("google.com")

    elif 'open pictures' in query:

        pictures = 'C:\\Users\\2019c\\Pictures'  # Your picture directory here

        action = os.listdir(pictures)
        os.open(action[0])

    elif 'play' in query:

        music_dir = "D:\\SONGS"  # Put your song directory's address here
        songs = os.listdir(music_dir)
        query = query.replace("play ", "")
        n = len(songs)
        for i in range(n):

            if query in songs[i].lower():
                print(songs[i])
                speak("Playing" + query)
                os.startfile(os.path.join(music_dir, songs[i]))
        break

    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" sir, The time is {strtime}")

    elif 'open pycharm' in query:
        speak("opening pycharm")
        pypath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.3\\bin\\pycharm64.exe"
        os.startfile(pypath)

        # you can open any application by giving its path to os.startfile function

    elif 'what is your name' in query:

        speak("no need to know my name, I am your assistant and my work is to obey you!")

    elif 'who are you' in query:
        speak("I am your assistant, how can you forget me?")

    elif 'hello' in query:
        speak("hi,how may I help you?")

    elif 'what can you do ' in query:
        speak("tell me something to do ")

    elif query == "jarvis":
        speak("Order Sir")

    elif 'quit' in query or 'bye' in query or "terminate" in query or "thank you" in query or "thanks" in query:
        speak("see you again")
        break

    elif 'search google' in query:
        speak("what do you want to search?")
        command = takeCommand()
        list = []
        speak("searching google")
        for i in search(command, tld="co.in", num=4, stop=4, pause=2):
            print(i)
            list.append(i)

        speak("wanna make me search for one of the urls in browser?")
        cmd = takeCommand()
        if 'yes' in cmd:
            speak("which one? ")
            ans = takeCommand()
            if 'first' in ans or 'I' in ans or '1' in ans:
                speak("searching")
                webbrowser.get(chrome_path).open_new_tab(list[0])
            if 'second' in ans or 'II' in ans or '2' in ans:
                speak("searching")
                webbrowser.get(chrome_path).open_new_tab(list[1])
            if 'third' in ans or 'III' in ans or '3' in ans:
                speak("searching")
                webbrowser.get(chrome_path).open_new_tab(list[2])
            if 'fourth' in ans or 'IV' in ans or '4' in ans:
                speak("searching")
                webbrowser.get(chrome_path).open_new_tab(list[3])

            else:
                exit
            break

        else:
            speak("ok")
            break

    elif 'open vs code' in query:
        speak('opening v s code')
        os.startfile(
            "C:\\Users\\2019c\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif 'open my facebook' in query:
        speak("opening your facebook")
        webbrowser.get(chrome_path).open("www.facebook.com/ritek.saxena.3")

    elif 'open my instagram' in query:
        speak("opening your instagram")
        webbrowser.get(chrome_path).open(
            "https://www.instagram.com/ritek_saxena/?hl=en")

    else:
        speak(f'searching {query} over the internet ')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print(results)
        speak(results)
