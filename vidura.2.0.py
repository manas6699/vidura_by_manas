import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Without runAndwait command, speech will not be audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("subho sokal , moharaj")

    elif hour >= 12 and hour < 17:
        speak(" subho dupur  , moharaj")

    else:
        speak("subho sondha , moharaj")

    speak("ami vidhura , ami upnar ki seba korte pari? ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"Lord said : {query}\n")  # User query will be printed.

    except Exception as e:
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query


        if'exit' in query:
            speak("Thank you very much sir , wish your day is fantabulous!")
            exit()


        elif'quit' in query:
            speak("Thank you very much sir , wish your day is fantabulous!")
            exit()

        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("opening youtube in your web browser")
            webbrowser.open("Youtube.com")


        elif 'google' in query:
            speak("opening google in your web browser")
            webbrowser.open("google.com")

        elif 'open music' in query:
            speak("Opening your awesome music files!")
            music_dir = 'E:\\code\\python\\vidura'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


       
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

