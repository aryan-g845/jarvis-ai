import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import time
import requests



# Speak function (always works)
def speak(text):
    engine = pyttsx3.init(driverName='sapi5')  # Windows voice engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0=male, 1=female (change if you want)
    engine.setProperty('rate', 170)  # speaking speed
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# for wikipedia Knowledge
def get_wikipedia_summary(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Title:", data["title"])
        print("Description:", data["extract"])
        speak(f"okey i tell about {query}")
        speak(data["extract"])
    else:
        print("Error:", response.status_code)

# Website opening
def open_website(query):
    query = query.lower()
    if "open youtube" in query:
        speak("okey sir, I opened YouTube")
        webbrowser.open("https://youtube.com")
        
    elif "open spotify" in query:
        speak("okey sir, I opened Spotify")
        webbrowser.open("https://spotify.com")
        
    elif "favourite song" in query:
        webbrowser.open("https://www.youtube.com/watch?v=tEMLsDzvbJo&list=RDtEMLsDzvbJo&start_radio=1")
        speak("okey sir, I opened your favorite song")
    elif "jay shri ram" in query:
        speak("Jay Shri Ram, Jay Shree Krishna")
    elif "smile" in query:
        speak("Haa,haa haa haa")



#Giving an argue as reply
def open_argue(query):
    query = query.lower()
    if "time" in query:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        speak(f"The current time is {current_time}")
    elif "today date" in query:
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        speak(f"Today's date is {current_date}")
    elif "who is your developer" in query:
        speak("Aaryan Goswami is my developer.")
    elif "tum kaise ho" in query:
        speak("Main theek hoon, aap kaise hain?")



# Windows apps opening
# open Explorer
def open_explorer(query):
    query = query.lower()
    if "file explorer" in query:
        os.system("explorer")
        speak("Opening File Explorer")
    elif "close explorer" in query:
        os.system("taskkill /im explorer.exe /f")
        speak("Closing File Explorer")

# open settings
def open_settings(query):
    query = query.lower()
    if "open settings" in query:
        os.system("start ms-settings:")
        speak("Opening Settings")
    elif "close settings" in query:
        os.system("taskkill /im SystemSettings.exe /f")
        speak("Closing Settings")        

# open task manager
def open_task_manager(query):
    query = query.lower()
    if "task manager" in query:
        os.system("taskmgr")
        speak("Opening Task Manager")
    elif "close task manager" in query:
        os.system("taskkill /im taskmgr.exe /f")
        speak("Closing Task Manager")


# open camera
def open_camera(query):
    query = query.lower()
    if "open camera" in query:
        os.system("start microsoft.windows.camera:")
        speak("Opening Camera")
    elif "close camera" in query:
        os.system("taskkill /im Camera.exe /f")
        speak("Closing Camera")

# open notepad
def open_notepad(query):
    query = query.lower()
    if "open notepad" in query:
        os.system("notepad")
        speak("Opening Notepad")
    elif "close notepad" in query:
        os.system("taskkill /im notepad.exe /f")    
        speak("Closing Notepad")
        
# open calculator
def open_calculator(query):
    query = query.lower()
    if "open calculator" in query:
        os.system("calc")
        speak("opening calculator") 
    elif "close calculator" in query:
        os.system("taskkill /im Calculator.exe /f")
        speak("Closing Calculator")

#open command prompt
def open_cmd(query):
    query = query.lower()
    if "open cmd" in query:
        os.system("start cmd")
        speak("opening command prompt")
    elif "close cmd" in query:
        os.system("taskkill /im cmd.exe /f")
        speak("Closing command prompt")

# open edge
def open_edge(query):
    query = query.lower()
    if "open edge" in query:
        os.system("start msedge")
        speak("Opening Microsoft Edge")
    elif "close edge" in query:
        os.system("taskkill /im msedge.exe /f")
        speak("Closing Microsoft Edge")

#open chrome
def open_chrome(query):
    query = query.lower()
    if "open chrome" in query:
        os.system("start chrome")
        speak("Opening Google Chrome")
    elif "close chrome" in query:
        os.system("taskkill /im chrome.exe /f")
        speak("Closing Google Chrome")

apps = {
    "explorer": open_explorer,
    "settings": open_settings,
    "task manager": open_task_manager,
    "camera": open_camera,
    "notepad": open_notepad,
    "calculator": open_calculator,
    "cmd": open_cmd,
    "edge": open_edge,
    "chrome": open_chrome
}

# Main loop
def app_run():
    recognizer = sr.Recognizer()
    speak("Initializing jarvis.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")

            if "jarvis" in query.lower():
                speak("Yes sir.")

            else:
                get_wikipedia_summary(query)
                open_argue(query)
                open_website(query)
                for name, func in apps.items():
                    func(query)

        except sr.WaitTimeoutError:
            print("Listening timed out. Try again.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except Exception as e:
            print(f"Error: {e}")

app_run()