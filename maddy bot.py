import pyttsx3
import speech_recognition as sr
import datetime
import time
import pywhatkit
import os
import requests
import webbrowser
import wikipedia
import sys


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[0].id)
    engine.setProperty('voices', voices[0].id)

    engine.say(audio)
    engine.runAndWait()
    print(audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(query)


    except:
        speak("please repeat your command sir ")

    return query
def greet():
    hour=int(datetime.datetime.now().hour)
    tt= time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak("good morning sir ")
        speak(tt)

    elif hour>=12 and hour<15:
        speak("good afternoon sir")
        speak(tt)

    elif hour>=15 and hour<18:
        speak("good evening sir ")
        speak(tt)

    else:

        speak("good night sir")
        speak(tt)

    speak("i am online sir, how can i help u sir")

def intro():
    speak(" i am maddy , artificial intelligence robot, created by sir Mathesh")



def notepad():
    speak("Opening Notepad")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
    os.startfile(path)

def close_notepad():
    speak("closing notepad")
    os.system("taskkill /f /im notepad.exe")

def cmd():
    speak("opening cmd")
    os.system("start cmd")

def close_cmd():
    speak("closing cmd")
    os.system("taskkill /f /im cmd.exe")

def word_document():
    speak("opening word document")
    path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007"
    os.startfile(path)

def close_word():
    speak("closing word document")
    os.system("taskkill /f /im winword.exe")

def excel_sheet():
    speak("opening excel sheet")
    path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
    os.startfile(path)

def close_excel():
    speak("closing excel sheet")
    os.system("taskkill /f /im excel.exe")

def steam():
    speak("opening steam")
    path="C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam"
    os.startfile(path)

def close_steam():
    speak("closing steam")
    os.system("taskkill /f /im steam.exe")

def epic_games():
    speak("opening epic games")
    path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher"
    os.startfile(path)

def close_epicgames():
    speak("closing epic games")
    os.system("taskkill /f /im EpicGamesLauncher.exe")

def downloads():
    speak("opening downloads")
    path="C:\\Users\\Admin\\Downloads"
    os.startfile(path)
def close_downloads():
    speak("closing downloads")
    os.system("taskkill /f /im downloads.exe")

def discord():
    speak("opening discord")
    path="C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord"
    os.startfile(path)

def close_discord():
    speak("closing discord")
    os.system("taskkill /f /im discord.exe")

def python():
    speak("Opening python")
    path="C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\IDLE (Python 3.10 64-bit)"
    os.startfile(path)



def ip_address():
    speak("finding your ip address ")
    ip = requests.get("https://api.ipify.org").text
    speak(f"your ip address is {ip}")

def google():
    speak("opening google")
    speak("what should i search on google, sir")
    qn = takecommand().lower()
    webbrowser.open(f"https://www.google.com/search?q={qn}")

def youtube():
    speak("opening youtube")
    webbrowser.open("www.youtube.com")

def play_youtube():
    speak("opening youtube")
    speak("what do u want to play on youtube")
    name = takecommand()
    speak('playing' + name)
    pywhatkit.playonyt(name)


def facebook():
    speak("opening facebook")
    webbrowser.open("www.facebook.com")

def gmail():
    speak("opening gmail")
    webbrowser.open("www.gmail.com")



def google_wikipedia():
    speak("opening wikipedia")
    speak("what do u want to search on wikipedia")
    qn = takecommand().lower()
    result = wikipedia.summary(qn, sentences=2)
    speak(f"according to wikipedia{result}")
    print(result)

def stop():
    speak("as u wish sir ,but i don't want to leave u sir, bye sir")
    sys.exit(0)




if __name__=="__main__":
    greet()
    while True:
        query = takecommand().lower()
        if "open notepad" in query:
            notepad()

        elif "close notepad" in query:
            close_notepad()

        elif "open cmd" in query:
            cmd()

        elif "close cmd" in query:
            close_cmd()

        elif "open word document" in query:
            word_document()

        elif "close word document" in query:
            close_word()

        elif "open excel sheet" in query:
            excel_sheet()

        elif "close excel sheet" in query:
            close_excel()

        elif "open steam" in query:
            steam()

        elif " steam close" in query:
            close_steam()

        elif "open epic games" in query:
            epic_games()

        elif "close epic games" in query:
            close_epicgames()

        elif "open download" in query:
            downloads()

        elif "close downloads" in query:
            close_downloads()

        elif "open discord" in query:
            discord()

        elif "close discord" in query:
            close_discord()

        elif "open python idle" in query:
            python()

        elif " ip address" in query:
            ip_address()

        elif "intro" in query:
            intro()

        elif "open google" in query:
            google()

        elif "open youtube" in query:
            youtube()

        elif "open facebook" in query:
            facebook()

        elif "open gmail" in query:
            gmail()

        elif "open wikipedia" in query:
            google_wikipedia()


        elif "u can leave" in query:
            stop()

        elif "play on youtube" in query:
            play_youtube()













