import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime
import wikipedia
import pyjokes
import random

engine=pyttsx3.init()
listener=sr.Recognizer()
guess=random.randint(1,100)

def speak(text):
  engine.say(text)
  engine.runAndWait()
if __name__=="__main__":
  speak("Initializing jarvis...")

#Function to process all the commands
def run_jarvis(command):
  print("Command->"+command)
  if 'play' in command:
    song=command.replace("play","")
    speak("playing" + song)
    print("playing" + song)
    pywhatkit.playonyt(song)
  elif 'open google' in command:
    webbrowser.open("https://google.com")
  elif "open facebook" in command:
     webbrowser.open("https://facebook.com")
  elif "open youtube" in command:
     webbrowser.open("https://youtube.com")
  elif "open instagram" in command:
     webbrowser.open("https://instagram.com")
  elif "time" in command:
    time=datetime.datetime.now().strftime('%I:%M %p')
    speak("The time is "+time)
    print(time)
  elif "date" in command:
    date=datetime.datetime.now().strftime('%A, %B %d, %Y')
    speak("The date is "+date)
    print(date)
  elif "who is" in command:
    person=command.replace("who is","")
    info=wikipedia.summary(person,1)
    speak(info)
    print(info)
  elif "what is" in command:
    object=command.replace("what is","")
    info=wikipedia.summary(object,1)
    speak(info)
    print(info)
    
  elif "who are you"in command or "what are you"in command:
    speak("Im jarvis, a virtual assistant, ready to assist you")

  elif"joke" in command:
    joke=pyjokes.get_joke()
    speak(joke)
    print(joke)

  elif"change voice" in command:
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    speak("This is my new voice")

  elif"let's play a game" in command:
     speak("guess the number")
     hear=listener.listen(source)
     game=listener.recognize_google(hear)
     game=game.lower()
     if "guess the number" in game:
       speak("I have a number in mind. Guess it")
       hears=listener.listen(source)
       games=listener.recognize_google(hear)
       games=game.lower()
       if(games==guess):
         speak("You have guessed the correct number")
         quit()
       elif(games>guess):
         speak("Go lower")
       else:
         speak("Go higher")
  else:
    speak("I don't know, i am not fully developed yet")

while True:
  try:
    with sr.Microphone() as source:
      print("Listening...")
      voice=listener.listen(source)
      command=listener.recognize_google(voice)
      command=command.lower()
      if "jarvis" in command:
        command=command.replace("jarvis","")
        run_jarvis(command)
        
  except:
    pass


