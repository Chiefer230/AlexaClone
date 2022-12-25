import speech_recognition as Sr
import pyttsx3 
import datetime
from winsound import Beep
from googletrans import Translator


global Flag 
translator = Translator()
Time = datetime.datetime.now()
#Listener is an object used to parse voice into Text
listener = Sr.Recognizer()
# Initialize the Engine for text to Speech
engine = pyttsx3.init()
#Commands Menu using The 'Text'(User Voice Input) to navigate different responses 
def Commands(Text):
    if 'change voice to' in Text:
        ChangeVoice(Text)
        print(Text)
    elif Text[0] == 'hello':
        TextToSpeech(f'Hello {Name}')
    elif 'how old are you' in Text:
        TextToSpeech('I am 1 years old')
    elif 'who are you'in Text:
        TextToSpeech('My Name is Luci, Created By Jordan Rivera to Showcase his programming Skills using multiple libraries. For Now I am Stuck on Jordans Desktop with hopes to some day become mobile.')
    elif 'play me a song' in Text:
        notes = {'C': 1635,
         'D': 1835,
         'E': 2060,
         'S': 1945,
         'F': 2183,
         'G': 2450,
         'A': 2750,
         'B': 3087,
         ' ': 37}
        melodie = 'CDEFG G AAAAG AAAAG FFFFE E DDDDC'
        for note in melodie:
             Beep(notes[note], 500)
    elif 'what time is it' in Text:
        if Time.hour > 12:
            RegularTime = Time.hour - 12
            TextToSpeech(f'{RegularTime,Time.minute}')
        else:
            TextToSpeech(f'{Time.hour,Time.minute}')
    elif 'Translate' in Text:
        TextToSpeech('What Would you like me to translate')
        Beep(2000,100)
        with Sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            TranslatedText =translator.translate(command,src ='en', dest= 'es') 
            print(TranslatedText.text)
            TextToSpeech(TranslatedText.text)
#Text To Speech Function used to Take text and output speech using the initialized engine from the Pyttsx3 Library      
def TextToSpeech(Text):
    engine.say(Text)
    engine.runAndWait()
#Function to Express Text to Speech
def ChangeVoice(Text):
    ListofVoices = engine.getProperty('voices')
    if 'change voice to male' in Text:
        engine.setProperty('voice',ListofVoices[0].id)
        TextToSpeech('This is now Set to the Male Voice')
    elif 'change voice to female' in Text:
        engine.setProperty('voice',ListofVoices[1].id)
        TextToSpeech('This is now Set to the Female Voice')
        print('This is now Set to the Female Voice')

def Run():
    try:
        Flag = 0

        with Sr.Microphone() as source:            
            TextToSpeech('I am Listening')
            Beep(2000,100)
            print("listening")
            # The Listener listens from the Microphone and binds it to a voice variable
            voice = listener.listen(source)
            # Uses the Google API to translate the voice(Speech) into Text 
            command = listener.recognize_google(voice)
            if 'bye Luci' in command:
                Flag = 1
            Commands(command)
    except:
        pass
    return Flag





TextToSpeech('Hello My Name is Luci, ask me limited questions for Now. Before we get started, What is your Name?')

with Sr.Microphone() as source:
    Beep(2000,100)
    voice = listener.listen(source)
    Name = listener.recognize_google(voice)
    if 'jay' in Name:
        TextToSpeech(f'Hello {Name}, How can I help you today sir?')
    else:
        TextToSpeech(f'Hello {Name}, How can I assist you Today?')
while True:
    if Run() == 1:
        TextToSpeech(f'GoodBye {Name}')
        break
    else:
        continue
    