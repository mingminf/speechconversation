import speech_recognition as sr
import pyttsx
import cv2
import msvcrt


# see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine = pyttsx.init('sapi5')
speech_engine.setProperty('rate', 150)


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
	with sr.Microphone(device_index=1) as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
		return recognizer.recognize_google(audio)
	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Recog Error; {0}".format(e))
	return ""



#commands = [("crop", "cropping", "cropped", "crops"), ("emphasize, emphasizes, emphasizing, emphasized, emphasis"), ("action", "actions"), ("label", "labels", "labelling", "annotate", "annotates", "annotating")]

def emphasizeImage():
    speak("emphasize which area?")

def calloutImage():
    speak("callout which area?")

def annotateImage():
    speak("what to annotate?")

def recordRegion():
    pass

def recordAction():
    speak("OK. Start recording in 5 seconds")

Done = False
while not Done:
    speak("How can I help you?")
    sentence = listen()
    #speak("I heard: " + sentence)
    if "emphasize" in sentence:
        emphasizeImage()
    elif "callout" in sentence:
        calloutImage()
    elif "annotate" in sentence:
        annotateImage()
    elif "action" in sentence:
        recordAction()
    elif "here" in sentence:
        recordRegion()
    elif "stop" in sentence:
        Done = True
    """if msvcrt.kbhit():
        Done = True"""

"""def onStart(name):
    print 'starting', name

def onWord(name,location,length):
    print 'word', name, location, length

def onEnd(name, completed):
    print 'finishing', name, completed
    if name == 'fox':
        speech_engine.say("what a lazy dog!", 'dog')
    elif name == 'dog':
        speech_engine.endLoop()


speech_engine.connect('started-utterance', onStart)
speech_engine.connect('started-word', onWord)
speech_engine.connect('finished-utterance', onEnd)
speech_engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
speech_engine.startLoop()"""
