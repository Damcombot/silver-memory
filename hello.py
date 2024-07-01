import streamlit as st
import speech_recognition as sr
import wikipedia

def recognize_speech_from_audio_file(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def search_wikipedia(query):
    result = wikipedia.summary(query, sentences=2)
    return result

st.title('Voice Assistant')

uploaded_file = st.file_uploader("Choose an audio file", type=['wav', 'flac'])

if uploaded_file is not None:
    query = recognize_speech_from_audio_file(uploaded_file)
    st.write(f"You said: {query}")
    result = search_wikipedia(query)
    st.write(result)
