import speech_recognition as sr
import re

def listen_once():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        numbers = re.findall(r'\d+', text)

        if numbers:
            expression = " + ".join(numbers)
            return expression
        else:
            return ""

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("API unavailable")
        return ""