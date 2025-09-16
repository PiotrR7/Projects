import speech_recognition as sr
import pyttsx3

# Inicjalizacja modułu rozpoznawania mowy
r = sr.Recognizer()

# Inicjalizacja modułu syntezy mowy
engine = pyttsx3.init()

# Funkcja do syntezy mowy
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Funkcja do rozpoznawania mowy
def recognize_speech():
    with sr.Microphone() as source:
        print("Mów teraz...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="pl-PL")
            print("Rozpoznano: " + text)
            return text
        except sr.UnknownValueError:
            print("Nie rozpoznano mowy")
            return ""
        except sr.RequestError as e:
            print("Błąd serwera: " + str(e))
            return ""

# Główna pętla programu
while True:
    # Rozpoznawanie mowy
    text = recognize_speech()
    
    # Sprawdzanie komend
    if "cześć" in text:
        speak("Cześć!")
    elif "jak się masz" in text:
        speak("Dobrze, dziękuję!")
    elif "do widzenia" in text:
        speak("Do widzenia!")
        break
