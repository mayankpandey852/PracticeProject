from email.mime import audio
import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning") 
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("Hey mayank,zira here,how may i help you?")


def takeCommand():
    #it takes command
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("I am listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("trying to recognise..")
            query = r.reconise_google(audio,Language='en-in')
            print(f"user said: ,{query}\n")

        except Exeption as e:
            print(e)
            print("say again")
            return "none"
        return query





if __name__=="__main__" :
    wishMe()  
    takeCommand()
