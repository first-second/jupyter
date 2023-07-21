import pyttsx3
engine = pyttsx3.init()
text = "Welcome back sir"
engine.setProperty("rate", 130)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[10].id)
engine.say(text)
engine.runAndWait()

