import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text now")
engine.runAndWait()
engine.stop()