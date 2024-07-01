import streamlit as st
#code---

st.set_page_config(page_title="Vadarly",page_icon=":part_alternation_mark:",layout="wide")

#images store---
image_path= "https://th.bing.com/th/id/OIP._dP2SPVcLwJ-r_uKSsbpkwHaEK?rs=1&pid=ImgDetMain"


#hidder--
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#hidder2--
hide_github_icon = """
<style>
    #GithubIcon {
        visibility: hidden;
    }
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


#Header---
with st.container():
            st.title(""" Welcome to _:blue[Vadarly]_ """)
            st.header("Vadarly is a ***voice assistant*** ")
            st.divider()
with st.container():
            left_column,right_column = st.columns(2)
            with left_column:
                        st.write("It uses :blue-background[NLP] and :red-background[CV] ")
                        st.write("It can predict the ***presence*** of user ")
#camera-roll-test-- 

#picture = st.camera_input("Take a picture")

#if picture:
    #st.image(picture)

#code-box--
st.code("""import speech_recognition as sr
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
""")

#image1---
col1 , col2 = st.columns([2, 1])
with col2:
            st.image(image_path,caption="")
with col1:
            st.write("Random Text")




st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
