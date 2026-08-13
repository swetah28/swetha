'''import speech_recognition as vc
a=vc.Recognizer()
with vc.Microphone() as source:
    print("speak now...")
    try:
        audio=a.listen(source,timeout=30)
        text=a.recognize_google(audio)
        print("i have said :",text)
    except vc.UnknownValueError:
        print(" did  not speak")
    except vc.RequestError:
        print("google not recognize")'''

import speech_recognition as sr
import pyttsx3
import webbrowser as wb

def speak():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("connected.....")
        try:
            audio=a.listen(source,timeout=10)
            rose=a.recognize_google(audio)
            return rose
        except sr.UnknownValueError:
             return " did  not speak"
        except sr.RequestError:
             return "google not recognize"

def type(text_to_speak):
    engine=pyttsx3.init()
    engine.setProperty("rate",100)
    engine.setProperty("volume",1.0)
    engine.say(text_to_speak)
    engine.runAndWait()
rose=speak()
print(rose)
if rose=="hi hello":
    type("this is livewire")
elif "google" in rose.lower():
    wb.open("https://www.google.com/search?q="+rose)


