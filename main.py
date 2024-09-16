import pyttsx3 as p
import speech_recognition as sr

# Initialize the text-to-speech engine

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # Adjust the speech rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to the second voice (usually female)
print(voices)

def speak(text):
    """Speak the provided text using pyttsx3"""
    engine.say(text)
    engine.runAndWait()

# Recognizer class
r = sr.Recognizer()

# Initial greeting by the voice assistant
speak("Hello there. I am APENDEKI PYANA, your voice assistant. How can I help you?")

# Listen to the user's response through the microphone
with sr.Microphone() as source:
    r.energy_threshold = 10000  # Capture even low voices in noisy environments
    r.adjust_for_ambient_noise(source, duration=1.5)  # Adjust for background noise
    print("Listening:")
    audio = r.listen(source)

    try:
        # Convert speech to text using Google API
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Respond based on recognized speech
        if "are you ok" in text.lower():  # Ensure case insensitivity and phrase matching
            speak("I am good, thanks for asking.")
            speak("Tell me, what can I do for you?")
        else:
            speak("I didn't understand that. Can you please repeat?")
    
    except sr.UnknownValueError:
        speak("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")


