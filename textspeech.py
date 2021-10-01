import pyttsx3
engine = pyttsx3.init()
engine. setProperty("rate", 150)
engine.say(
    "jon snow avenge the red wedding,he is the white wolf,the king in the north")
engine.runAndWait()
engine.stop()

// pyttsx3 can be used ofline 
