import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listerner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listerner.listen(source)
            command=listerner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace("alexa","")
    except:
        pass
    return command

def run_alexa():
    command = alexa_command()
    if "play" in command:
        song = command.replace("play","")
        talk("Playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print("Current time is %d",time)
        talk("Current time is "+time)
    elif "superstar" in command:
        person = command.replace("superstar","")
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
        
        
run_alexa()
