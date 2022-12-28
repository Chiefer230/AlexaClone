import speech_recognition as Sr
import pyttsx3 
import datetime
from winsound import Beep
from googletrans import Translator
import json
import random

# Flag to determine the Current State of the AI
global Flag

#Translator Object used to Translate Inputted Text to outputted voice Data 
translator = Translator()
#Time Object used to get the Current Time
Time = datetime.datetime.now()
#Listener is an object used to parse voice into Text
listener = Sr.Recognizer()
# Initialize the Engine for text to Speech
engine = pyttsx3.init()


class CommandsData:
    #Initialize the Json data of commands  
    ListofCommands = json.loads(open('Commands.json').read())
    Greetings =[]
    GreetingResponse = []
    GoodByes = []
    GoodbyeResponse = []
    Age = []
    AgeResponse = []
    Songs = []
    SongsResponse = []
    Options = []
    OptionsResponse = []

    for phrase in ListofCommands["Commands"]:
        UserInput = phrase["UserInputs"]
        Response = phrase["Responses"]
        for tag in phrase["tag"]:
            print(tag)
            if tag == "Greetings":
                Greetings = UserInput
                print(Greetings)
                GreetingResponse = (Response)
                print(GreetingResponse)
            elif tag == "GoodByes":
                GoodByes = (UserInput)
                print(GoodByes)
                GoodbyeResponse = (Response)
                print(GoodbyeResponse)
            elif tag == "Age":
                Age = (UserInput)
                print(Age)
                AgeResponse = (Response)
                print(AgeResponse)
            elif tag == "Songs":
                Songs = (UserInput)
                print(Songs)
                SongsResponse = (Response)
                print(SongsResponse)
            elif tag == "Options":
                Options = UserInput
    @staticmethod
    def RandomRepsonse(ResponseList):
        Choice = random.choice(ResponseList)
        return Choice 
#Commands Menu using The 'Text'(User Voice Input) to navigate different responses
#Takes an external Object where the data for Predicted User Responses are stored and Default responses are produced
def Commands(Text):
    Command = CommandsData()
    print(Text)
    if Text in Command.GoodByes:
        Response = Command.RandomRepsonse(Command.GoodbyeResponse)
        TextToSpeech(Response)
        Flag = 1
    elif Text in Command.Greetings:
        Response = Command.RandomRepsonse(Command.GreetingResponse)
        TextToSpeech(Response)
    elif Text in Command.Age:
        Response = Command.RandomRepsonse(Command.AgeResponse)
        TextToSpeech(Response)
    elif 'who are you'in Text:
        TextToSpeech('My Name is Luci, Created By Jordan Rivera to Showcase his programming Skills using multiple libraries. For Now I am Stuck on Jordans Desktop with hopes to some day become mobile.')
    elif Text in Command.Songs:
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

    elif Text in Command.Options:
        if "what time is it" or "what is the time" in Text:
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
        elif 'change voice to' in Text:
            ChangeVoice(Text)
            print(Text)
        
    else:
        TextToSpeech('I do not Recognize this command')
    return Flag






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
#Run Method used to begin the second state of the AI where more specific request can be asked
#A microphone is used to gather voice commands to be converted into text where it will be used to perform operations
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
            Flag = Commands(command)
    except:
        pass
    return Flag



if Time.hour<=12:
    TextToSpeech('Good Morning')
elif Time.hour>=13:
    TextToSpeech('Good Afternoon')
#Beg State of the AI where it is introduced and the user introduces their name to the AI to be stored
TextToSpeech('Hello My Name is Luci, ask me limited questions for Now. Before we get started, What is your Name?')

with Sr.Microphone() as source:
    Beep(2000,100)
    voice = listener.listen(source)
    Name = listener.recognize_google(voice)
    print(Name)
    if 'jay' in Name:
        TextToSpeech(f'Hello {Name}, How can I help you today sir?')
    else:
        TextToSpeech(f'Hello {Name}, How can I assist you Today?')
#Loop the Second state of the Machine until the Run function returns a terminal flag to end the program
while True:
    if Run() == 1:
        break
    else:
        continue
    