
import streamlit as st
from agent.chatbox import get_AI_reponse
import speech_recognition as sr
import fitz

uploaded = st.file_uploader("upload a file ",type=["pdf","txt"])
if uploaded is not None:
    if uploaded.name.endswith("txt"):
        uploaded_text = uploaded.read().decode("utf-8")
    else:
        pdf_bytes = uploaded.read()
        doc = fitz.open(stream = pdf_bytes,filetype="pdf") 
        uploaded_text = ""
        for page in doc:
            uploaded_text += page.get_text()


    user_input = st.text_input("What's on your mind today")     
 
           
    audio_file = st.audio_input("click on the mic to start speaking 🗣️")
    if audio_file:
        
        recognizer = sr.Recognizer()
    
        with sr.AudioFile(audio_file) as source:
            audio_data =recognizer.record(source)
            user_input = recognizer.recognize_google(audio_data,language ="en-US")
                     
  
            
    if user_input :
        try:
            with st.spinner("Searching ..."):
                 st.subheader("💡Answer ...") 
                 st.write(get_AI_reponse(user_input,uploaded_text))  
        except sr.RequestError:
            st.error("No internet connection please check your network")
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio. Please try again.") 
        except Exception as e:
            st.error(f"We have a value error {e}")
else:
    
    user_input = st.text_input("What's on your mind today")
    audio_file = st.audio_input("click on the mic to start speaking 🗣️")
    if audio_file:
        
        recognizer = sr.Recognizer()
    
        with sr.AudioFile(audio_file) as source:
            audio_data =recognizer.record(source)
            user_input = recognizer.recognize_google(audio_data,language ="en-US")
     
    if user_input :
        try:
            with st.spinner("Searching ..."):
                 st.subheader("💡Answer ...") 
                 st.write(get_AI_reponse(user_input,uploaded_text=None))  
        except sr.RequestError:
            st.error("No internet connection please check your network")
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio. Please try again.") 
        except Exception as e:
            st.error(f"We have a value error {e}")
    






        



          