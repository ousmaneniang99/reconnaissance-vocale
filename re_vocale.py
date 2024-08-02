import streamlit as st
import speech_recognition as sr

def transcribe_speech(api, language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            if api == "Google":
                text = r.recognize_google(audio_text, language=language)
            elif api == "Sphinx":
                text = r.recognize_sphinx(audio_text, language=language)
            else:
                text = "Unknown API selected"
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not get that."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def save_transcription(text):
    with open("transcription.txt", "a") as file:
        file.write(text + "\n")

def main():
    st.title("Enhanced Speech Recognition App")

    st.write("Select the Speech Recognition API:")
    api = st.selectbox("API", ["Google", "Sphinx"])

    st.write("Select the language:")
    language = st.selectbox("Language", ["en-US", "fr-FR", "es-ES", "de-DE"])

    if st.button("Start Recording"):
        text = transcribe_speech(api, language)
        st.write("Transcription: ", text)
        if st.button("Save Transcription"):
            save_transcription(text)
            st.success("Transcription saved!")

if __name__ == "__main__":
    main()
