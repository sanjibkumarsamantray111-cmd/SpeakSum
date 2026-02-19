import speech_recognition as sr
from calculator_core import VoiceCalculatorCore

calc = VoiceCalculatorCore()
r = sr.Recognizer()

print("🎤 Voice Calculator Started")
print("Say numbers.")
print("Say 'total' to get result.")
print("Say 'exit' to quit.\n")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-US")
        print("You said:", text)

        text_clean = text.lower().strip()

        if "exit" in text_clean:
            break

        elif "total" in text_clean:
            print("Total:", calc.get_total())

        else:
            expression = calc.add_spoken_number(text_clean)
            print("Expression:", expression)

    except Exception as e:
        print("Error:", e)