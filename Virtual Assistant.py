import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia

sonal =pyttsx3.init('sapi5')
voices=sonal.getProperty('voices')

# pirnt(voices[0].id) This line is used to check which voice is male and which is female
sonal.setProperty('voice',voices[1].id)

def speak(audio):
    sonal.say(audio)
    sonal.runAndWait()
    
def welcomeMessage():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('Good morning')
    elif hour>=12 and hour <18:
        speak('Good afternoon')
    else:
        speak('Good Evening')
    speak("I am Sonal your Virtual assistant,how may I assist you")    

def Command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm Listening..")
        r.pause_threshold=1     # it will wait for 1 min
        
        audio=r.listen(source)
    try:
        speak('Recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f"User said{query}")
    except Exception as e:
        speak("Soory I did not hear you, can you say that again")
        return "None"
    return query    

if __name__ == "__main__":
    welcomeMessage()               #calling function
    while True:
        query=Command().lower()
        if "Chrome" in query:
            speak("Opening Chrome for you sir")
            os.system('Chrome')
        elif 'youtube' in query:
            speak("Opening Youtube for you")
            webbrowser.open("https://youtube.com/")
        elif 'Gmail' in query:
            speak("Opening Gmail for you")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")    
        elif 'exit' in query:
            speak('Thank you for using me,Have a great day')
            break
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)    
    


