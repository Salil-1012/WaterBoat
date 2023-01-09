#                                SALIL's ROBOT  ARTIFICAL INTELLIGENCE ----> WATER-BOAT 
import pyttsx3                                 
import datetime                                
import speech_recognition as sr               
import webbrowser                             
import os                                      
import time                                                
import wikipedia                               
from Downloader import Downloader
import subprocess
from os import startfile

System_engine = pyttsx3.init('sapi5') 
voices = System_engine.getProperty('voices')
System_engine.setProperty('voices', voices[0].id) 


def speak_my_boy(m):
    System_engine.say(m)
    System_engine.runAndWait()
def Bless_me_boy():
    time_in_hour = int(datetime.datetime.now().hour)
    if time_in_hour >= 0 and time_in_hour < 12: 
        speak_my_boy("Good Morning , Sir")
    elif time_in_hour >= 12 and time_in_hour < 18: 
        speak_my_boy("Good Afternoon  , Sir")
    else:
        speak_my_boy("Good Evening, Sir ")
    speak_my_boy( " I am Robot, Speed 1 terahertz, memory 1 zeta byte. Please tell me how may i help you ")

def Intro_sys():
    speak_my_boy(
        "Wellllll, I speak , therefore I am.  I'm  ACET's  Invention , his personal productivity assistant,"
        " I am a machine robot name Waterboat. I can do everything in your system,"
        "I am a virtual assistant, that helps like any other human assistant,"
        "  People like me, because of my personalities , my way of understanding them,"
        "My basic speed is Speed 1 terahertz, memory 1 zeta byte. "
        "And I my here to help you,Sir "
    )

def Making_notes():
    a = input("Enter the text here ---->".title())  
    System_engine.say(a)
    System_engine.runAndWait()

def Voice_to_txt():
    takes = sr.Recognizer()
    with sr.Microphone() as source:
        print(".......LISTENING ........")
        sound = takes.listen(source)
    try:
        print("WAIT I AM TYPING..... ")
        problem=takes.recognize_google(sound,language='en-in')
        print(f"YOU SAID  {problem}")
        with open('NOTES.txt',"a") as file:
            file.write(problem)
            file.write("\n")
            print("SUCCESSFULLY WRITEEN IN THE FILE NOTES ")
            file.close()
    except Exception as e:
        print("SPEAK AGAIN YOUR VOCIE NOT AUDIBLE")

def Intro_me():
    speak_my_boy(
        "I guess, you are a human belong to the planet earth , Am I right ")


def OBEY_MY_WORDS():
    takes = sr.Recognizer()
    with sr.Microphone() as source:
        print("...........Yes you are audaible. Please speak........")
        speak_my_boy("Ask your query")
        takes.pause_threshold = 0.5
        sound = takes.listen(source)
    try:
        print("...........Under Process........")
        speak_my_boy("PLEASE WAIT")
        problem = takes.recognize_google(sound, language='en-in')
        print(f"your query is --> {problem}\n")
    except Exception as e:
        print('............SAY IT AGAIN PLEASE.......... ')
        return "None"
    return problem


def OBEY_MY_WORDS2():
    problem = input("Enter the query --->")
    
    return problem

def FirstUser(h):
    print(" ...............YOU CAN ASK ME ABOUT...........  ")
    speak_my_boy("YOU CAN ASK ABOUT  ")
    time.sleep(1) 
    print(" 1) ------> ABOUT MYSELF")
    speak_my_boy("about myself")
    time.sleep(1)
    print(" 2) -------> I also introduce you ")
    speak_my_boy("I also introduce you ")
    time.sleep(1)
    print(" 3) -------> I will tell about the weather outside ")
    speak_my_boy("I will tell about the weather outside")
    time.sleep(1)
    print(" 4) -------> I will tell about the current time ")
    speak_my_boy("I will tell about the current time")
    time.sleep(1)
    print(" 5) ------->  Google , Youtube, Whatsapp , Gmail, College ")
    speak_my_boy("I will open  application like google , youtube , whatsapp , gmail for you ")
    time.sleep(1)
    print(" 6) ------->  JUST SAY MAKE THE NOTES ")
    speak_my_boy("I ALSO SPEAK THE NOTES YOU MAKE  ") 
    time.sleep(1)
    print(" 7) ------->  JUST SAY WRITE THE NOTES ")
    speak_my_boy("I ALSO WRITE THE NOTES YOU SPEAK  ") 
    time.sleep(1)
    print(" 8) ------->   JUST SAY MY PC ")
    speak_my_boy("OPEN YOUR OPERATING SYSTEM ") 
    time.sleep(1)
    print(" 9) ------->  TRANSLATE ")
    speak_my_boy("I ALSO TRANSLATE YOUR WORDS") 
    time.sleep(1)
    print(" 10) ------->  WIKIPEDIA ")
    speak_my_boy("I ALSO SEARCH  YOUR WORDS ON WIKIPEDIA") 
    time.sleep(1)
    print(" 11) ------->  PLAY GAME ")
    speak_my_boy("YOU CAN ALSO PLAY THE GAME")
    speak_my_boy("PRESS ONE TO WRITE THE QUERY AND PRESS TWO TO SPEAK THE QUERY")
    time.sleep(1)

if __name__ == "__main__":
    
    print("..................THIS IS MY PERSONAL ASSISTAINT...........")
    print("................This help us to do the things in just one word......... ")
    Bless_me_boy()
    print("PRESS ANY KEY TO USE THE WATERBOT")
    print("OR")
    print("TYPE 'help' TO GET MORE INFORMATION ABOUT THIS BOT")
   
    System_engine.say("PRESS ANY KEY TO USE THE WATERBOT")
    System_engine.say(" OR TYPE 'help' TO GET MORE INFORMATION ABOUT THIS BOT")
    System_engine.runAndWait()
     
    
    helpdesk = input(".................Type 'Help'  If You Are First Time User OR PRESS ANY KEY .............. -->  ").lower()

    if(helpdesk=="help"):
        FirstUser(helpdesk)
    
    System_engine.say("PRESS ONE TO WRITE THE QUERY AND PRESS TWO TO SPEAK THE QUERY")
    print("PRESS ONE TO WRITE THE QUERY AND PRESS TWO TO SPEAK THE QUERY")
    print("1  --->    TYPE")
    print("2  --->   SPEAK")
    System_engine.runAndWait() 
    a= int(input("Enter the number"))
    if(a==1):
        while True:
            problem = OBEY_MY_WORDS2().lower()
            if 'time' in problem:
                t = datetime.datetime.now().strftime('%H:%M:%S')
                print(f"the time is {t}")
                speak_my_boy(f"Sir, the time is {t}")
                
            elif 'tell about yourself' in problem:
                Intro_sys() 

            elif 'google' in problem:
                webbrowser.open("https://www.google.co.in//")
            
            elif 'college' in problem:
                webbrowser.open("www.agcamritsar.in//")

            elif 'quit' in problem:
                speak_my_boy("Ok salil sir Good Byee, Have a NIce day...")
                print("..........THIS IS PROGRAM IS PERSONALLY MADE BY SALIL CHANDAN.......")
                print("************THANKU YOU**********  ".center(50))
                print("")
                print("...............** BYEE **..............".center(50))
                time.sleep(3)
                exit()

            elif 'youtube' in problem:
                webbrowser.open("https://www.youtube.com//")

            elif 'my pc' in problem:
                os.startfile("D:\\") 

            elif 'music' in problem:
                System_engine.say("ENJOY YOUR SONG SIR")
                System_engine.runAndWait()
                startfile("C:\\Users\\asd\\Music\\Video Projects")

            elif 'game' in problem:
                subprocess.call(" python game.py 1", shell=True)

            elif 'introduce me' in problem:
                Intro_me()

            elif 'yes' in problem:
                speak_my_boy("Yes, thank u sir , so now tell, how may i help u")

            elif 'gmail' in problem:
                webbrowser.open("https://mail.google.com//mail//u//0//")

            elif 'weather' in problem:
                webbrowser.open(
                    "https://www.google.com//search?client=firefox-b-d&q=weather+today+in+amritsar")

            elif 'make the notes' in problem:
                Making_notes()

            elif 'whatsapp' in problem:
                webbrowser.open("https://web.whatsapp.com//")
            
            elif 'write the notes' in problem:
                Voice_to_txt()
            
            elif 'translate' in problem:
                speak_my_boy("What do you want to translate ")
                a= input("Enter the name")
                translator= Translator(from_lang="english",to_lang="hindi")
                translation = translator.translate(a)
                print (translation)
        
            elif 'wikipedia' in problem:
                print("Searching wikipedia.......")
                results = wikipedia.summary(problem,sentences=2)
                print(results)
                speak_my_boy("According to wikipedia ")
                speak_my_boy(results)
            
            elif 'dashboard' in problem:
                webbrowser.open_new_tab("http://112.196.50.43/login.asp")
            
            elif 'download' in problem:
                subprocess.call(" python Downloader.py 1", shell=True)
            
    
    
            
            
    if(a==2):
        while True:
            problem = OBEY_MY_WORDS().lower()
            if 'time' in problem:
                t = datetime.datetime.now().strftime('%H:%M:%S')
                print(f"the time is {t}")
                speak_my_boy(f"Sir, the time is {t}")
                
            elif 'tell about yourself' in problem:
                Intro_sys() 

            elif 'google' in problem:
                webbrowser.open("https://www.google.co.in//")
            
            elif 'college' in problem:
                webbrowser.open("www.agcamritsar.in//")

            elif 'quit' in problem:
                speak_my_boy("Ok salil sir Good Byee, Have a NIce day...")
                print("..........THIS IS PROGRAM IS PERSONALLY MADE BY SALIL CHANDAN.......")
                print("************THANKU YOU**********  ".center(50))
                print("")
                print("...............** BYEE **..............".center(50))
                time.sleep(3)
                exit()

            elif 'youtube' in problem:
                webbrowser.open("https://www.youtube.com//")

            elif 'my pc' in problem:
                os.startfile("D:\\") 

            elif 'music' in problem:
                System_engine.say("ENJOY YOUR SONG SIR")
                System_engine.runAndWait()
                startfile("C:\\Users\\asd\\Music\\Video Projects")
                # startfile("DESIRES - AP DHILLON  GURINDER GILL.mp4")

            elif 'game' in problem:
                subprocess.call(" python game.py 1", shell=True)

            elif 'introduce me' in problem:
                Intro_me()

            elif 'yes' in problem:
                speak_my_boy("Yes, thank u sir , so now tell, how may i help u")

            elif 'gmail' in problem:
                webbrowser.open("https://mail.google.com//mail//u//0//")

            elif 'weather' in problem:
                webbrowser.open(
                    "https://www.google.com//search?client=firefox-b-d&q=weather+today+in+amritsar")

            elif 'make the notes' in problem:
                Making_notes()

            elif 'whatsapp' in problem:
                webbrowser.open("https://web.whatsapp.com//")
            
            elif 'write the notes' in problem:
                Voice_to_txt()
            
            elif 'translate' in problem:
                speak_my_boy("What do you want to translate ")
                a= input("Enter the name")
                translator= Translator(from_lang="english",to_lang="hindi")
                translation = translator.translate(a)
                print (translation)

            
            elif 'wikipedia' in problem:
                print("Searching wikipedia.......")
                results = wikipedia.summary(problem,sentences=5)
                print(results)
                speak_my_boy("According to wikipedia ")
                speak_my_boy(results)
            
            elif 'dashboard' in problem:
                webbrowser.open_new_tab("http://112.196.50.43/login.asp")
            
            elif 'download' in problem:
                subprocess.call(" python Downloader.py 1", shell=True)
            
    
               

                
    
            
            
