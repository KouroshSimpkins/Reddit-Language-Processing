import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text now")
engine.save_to_file("I will speak this text now", "test.mp3")
engine.runAndWait()
engine.stop()