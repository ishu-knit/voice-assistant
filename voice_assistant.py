import pyttsx3                
import wikipedia             
import speech_recognition    
import webbrowser
import os
import datetime
import smtplib
import ssl


def speak(x):
    z=pyttsx3.init()
    z.setProperty('rate',128)
    z.say(x)
    z.runAndWait()

def audio():

    with speech_recognition.Microphone() as source:
        
       l=speech_recognition.Recognizer().listen(source ) 
       
       said=""

       said= speech_recognition.Recognizer().recognize_google(l)
        
	   
       return(said)

       

# webbrowser.open("index.html", "r")
speak("hello sir ")
w=audio()
y=w.lower()

if "wikipedia" in y:

  speak("here are the result of your search")
  x = wikipedia.summary(w, sentences=1 )
  speak(x)

if y== "open youtube" :
        speak("opening youtube")
        webbrowser.open("youtube.com")
      

elif y== "open notepad":
        speak(" Opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")
        

elif y== "play music":
        y=os.listdir("D:\\music")
        os.startfile(os.path.join("D:\\music",y[0]))

elif " time" in y:
        y=datetime.datetime.now().strftime("%H:%M")
        print(y)
        speak(f"the time is {y}")


elif "send email" in y:

        speak("how do u  want to send email  ,through text or speak")
        p=audio()
        if ("text" in p):
            speak("write what you want to send")
            message = input()
        if("speak" in p):
            w=audio()
            y=w.lower()
            message=y

        context=ssl.create_default_context()

        
        print("Starting to send")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login("jink93854@gmail.com", "jinkazama9#")
            server.sendmail("jink93854@gmail.com", "ishu.20226@knit.ac.in",message)
        speak("successfully send")
        print("sent email!")
# elif 

elif y == "exit":
        speak("thanks you sir ")
        exit()
        
