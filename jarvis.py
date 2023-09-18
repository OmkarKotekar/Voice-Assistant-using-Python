import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >=0 and hour<12):
        speak("Good Morning!")

    elif(hour>=12 and hour<16):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your voice assistant. Please tell me how may I help you")
def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("okotekar@gmail.com", "OmkarK@7")
    server.sendmail("okotekar@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    speak("Hello Omkar")
    wishMe()
    while(True):
        query = takeCommand().lower()
        #logic for executing task based on query
        if('wikipedia' in query):
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif('open youtube' in query):
            webbrowser.open("youtube.com")

        elif('open google' in query):
            webbrowser.open("google.com")

        elif('open stackoverflow' in query):
            webbrowser.open("stackoverflow.com")

        elif('open tcet' in query):
            webbrowser.open("tcetmumbai.com")

        # elif('play music' in query):
        #     music_dir = 'D:\\my music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        
        elif('time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif('code' in query):
            codePath = "D:\\python\\Microsoft VS Code"
            os.startfile(codePath)

        elif('email to okotekar' in query):
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "okotekar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was unable to send the email!")

        elif('quit' in query):
            speak("Bye Omkar. Nice meeting you...")
            exit()

