import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import sys

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""
    except Exception as ex:
        print("Error:", ex)
        return ""

# Function to greet user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

# Function to respond to commands
def respond(command):
    if "hello" in command:
        speak("Hi there! How can I assist you today?")
    elif "how are you" in command:
        speak("I'm doing well, thank you for asking!")
    elif "what is your name" in command:
        speak("My name is Assistant. How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query :
         try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, " + results)
         except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple interpretations for " + query + ". Please be more specific.")
         except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information about " + query)
    elif "goodbye" in command or "bye" in command:
        speak("Goodbye! Have a great day.")
        sys.exit()
    else:
        speak("Sorry, I didn't understand that command. Can you please repeat?")

# Main function to execute the assistant
def main():
    greet()
    while True:
        command = listen()
        respond(command)

if __name__ == "__main__":
    main()
