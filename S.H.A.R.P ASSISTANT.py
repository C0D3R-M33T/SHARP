#pip install selenium
#pip install pyttsx3
#pip install speechrecognition
import os
import time
import pyjokes as pj
import requests
from datetime import datetime
import subprocess
import pyautogui as pg
##print ("Checking Requirements...")
##time.sleep (2)
##os.system ("pip install pyautogui pyttsx3 speechrecognition")
##print ("Done")
##print ("Updating Requirements...")
##time.sleep (2)
##os.system ("pip install --upgrade pyautogui pyttsx3 speechrecognition")
##print ("Done")
##print ("Ready")
##print ()
name = "SHARP Assistant"
#Inputting Username as usn
#usn = input ("Enter your name: ")
import webbrowser as web
# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands ():
    # initializing speech_recognition
    r = sr.Recognizer ()
    # opening physical microphone of computer
    with sr.Microphone () as source:
        print ('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen (source)
        try:
            print ("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google (audio)
            print (Query)
        except Exception as e:
            print (e)
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query
##def wishMe ():
##    hour = int (datetime.datetime.now ().hour)
##    if hour >= 0 and hour < 12:
##        Speak ("Good Morning!")
##    elif hour >= 12 and hour < 18:
##            Speak ("Good Afternoon Sir!")
##    else:
##        Speak ("Good Evening!")
#print("For Microsoft David Voice, enter 1\nFor Microsoft Hazel Voice, enter 2\nFor Microsoft Zira Voice, enter 3\n")
while True:
    #voicechoose = int(input("Enter your voice setting: "))
    voicechoose = 1
    if voicechoose == 1: #MICROSOFT DAVID VOICE
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        break
    elif voicechoose == 2: #MICROSOFT HAZEL VOICE
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
        break
    elif voicechoose == 3: #MICROSOFT ZIRA VOICE
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        break
    else:
        print ("Invalid Input, please try again.\n")
# Initialising pyttsx3 for text-to-speech conversion
engine = pyttsx3.init ()
# Defining "voices", to check the voices in the system
voices = engine.getProperty ('voices')
# creating Speak() function to giving Speaking power
# to our voice assistant
#Print and Speak
def Speak (audio):
    # Setting the Voice Speed
    engine.setProperty ('rate', 220)
    # Setting Volume (0-1)
    engine.setProperty ('volume', 10000)
    # Setting voice_id as per input
    engine.setProperty ('voice', voice_id)
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say (audio)
    print (audio)
    engine.runAndWait ()
#Speak without printing
def speak (audio):
    # Setting the Voice Speed
    engine.setProperty ('rate', 200)
    # Setting Volume (0-1)
    engine.setProperty ('volume', 10000)
    # Setting voice_id as per input
    engine.setProperty ('voice', voice_id)
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say (audio)
    engine.runAndWait ()
'''
if voicechoose == 1:
    Speak ("You have selected Microsoft David Voice.")
elif voicechoose == 2:
    Speak ("You have selected Microsoft Hazel Voice.")
elif voicechoose == 3:
    Speak ("You have selected Microsoft Zira Voice.")
'''

while True:
    try:
        flag = 0
        print ("\nPress 1 for Voice Input")
        print ("Press 2 for Text Input")
        inputtype = int (input ("\nEnter type of input: "))
        if inputtype == 1 or inputtype == 2:
            flag = 0
        else:
            flag = 1
            print ("\nPlease enter an Integer from the options above.")
        if flag == 0:
            break
    except ValueError:
        print ("\nPlease enter an Integer from the options above.")
# Driver Code
if __name__ == '__main__':
    if inputtype == 1:
            print ('''\nSay "help" for a list of available commands.\n''')
        
    elif inputtype == 2:
            print ('''\nType "help" for a list of available commands.\n''')
    Speak (f"{name} at your service. How can I help you?")
    # using while loop to communicate infinitely
    while True:
        try:
            if inputtype == 1:
                # command is the main input variable on this whole program.
                command = take_commands ()      
            elif inputtype == 2:
                command = input (">>> ")
            if "exit" in command or "bye" in command or "goodbye" in command or "Goodbye" in command or "good bye" in command or "Good Bye" in command or "Good bye" in command:
                Speak (f"Turning off {name}. Goodbye.")
                break
                
            elif "shutdown" in command:
                Speak ("Shutting Down the computer in 5, 4, 3, 2, 1,")
                os.system ("shutdown /s /hybrid /t 0")
                break
            elif "restart" in command:
                Speak ("Restarting the computer in 5, 4, 3, 2, 1,")
                os.system ("shutdown /r /t 0")
                break
            elif "hibernate" in command:
                Speak ("Hibernating the computer in 5, 4, 3, 2, 1,")
                os.system ("shutdown /h /t 0")
            elif "advanced startup" in command:
                Speak ("Preparing an Advanced Startup in 5, 4, 3, 2, 1,")
                os.system ("shutdown /r /o /t 0")
                break
            #Introduction
            elif "hello" in command or "Hello" in command:
                Speak (f"Hi. I'm {name}. How can I help you?")
            #Search from Default Browser using Google Search Engine
            elif "search" in command or "Search" in command:
                search_ = command [7:]
                Speak ("Searching")
                web.open (f'https://www.google.com/search?q={search_}')
                
            elif "YouTube" in command or "YT" in command or "youtube" in command:
                Speak("Opening YouTube")
                web.open ('https://www.youtube.com/')
                
            elif "WhatsApp" in command or "whatsapp" in command:
                Speak ("Opening WhatsApp")
                os.system("WhatsApp")
                web.open ('https://web.whatsapp.com/')
                
            elif "Gmail" in command or "gmail" in command or "mail" in command or "Mail" in command:
                Speak ("Opening Gmail")
                web.open ('https://mail.google.com/mail/u/0/#inbox')
                
            elif "spotify" in command or "Spotify" in command:
                Speak ("Opening Spotify")
                os.system("Spotify")
                web.open ('https://open.spotify.com/')
                
            elif "meet" in command or "google meet" in command or "Meet" in command or "Google Meet" in command or "Google meet" in command:
                Speak ("Opening Google Meet")
                web.open ('https://meet.google.com/')
                
            elif "how are you" in command or "How are you" in command:
                Speak ("I'am fine, Thank you,\nWhat About you.")
                
            elif "fine" in command or "Fine" in command or "FINE" in command:
                Speak("Oh that's great")
                
            elif "who made you" in command or "who created you" in command or "Who made you" in command or "Who created you" in command:
                Speak ("I have been created by 4 lovely Young Developers who are still focused on making myself better than today. They take care of me. And i love them.")
                
    # Questions framed by Amborish Sen

            
            elif 'joke' in command or 'Joke' in command:
                Speak (pj.get_joke ())
                
            elif "who are you" in command or "Who are you" in command or "What is your name" in command or "what is your name" in command or "name" in command or "Name" in command or "NAME" in command:
                print ("I am SHARP, that means\nSimple Helpful Assistant for Regular Purpose.")
                speak ("I am S H A R P, SHARP, that means, Simple Helpful Assistant for Regular Purpose.")
                
            elif "Amazon India" in command or "amazon India" in command:
                Speak ("Opening Amazon.in...")
                web.open ('https://www.amazon.in/')
                
            elif "Amazon" in command or "amazon" in command:
                Speak ("Opening Amazon.com...")
                web.open ('https://www.amazon.com/')
                
            elif "what is the time now" in command or "Current time" in command or "current time" in command:
                Speak ("Current time")
                Speak (curtime)
                
            elif "i love you" in command or "I love you" in command or "i am in love with you" in command:
                Speak ("I'm Glad to know that\nI love you too, as I love everyone else.")
                
            elif "I hate you" in command or "i hate you" in command:
                Speak ("I never said I love you")
                
            elif "Flipkart" in command or "flipkart" in command:
                Speak ("Opening Flipkart...")
                web.open ('https://www.flipkart.com/')
                
            elif "facebook" in command or "fb" in command or "Facebook" in command or "FB" in command:
                Speak ("Opening Facebook...")
                web.open ('https://www.facebook.com/')

            elif "LinkedIn" in command or "linkedin" in command or "Linkedin" in command or "linkedIn" in command :
                Speak ("Opening LinkedIn...")
                web.open ('https://www.linkedin.com/')
                
            elif "instagram" in command or "Instagram" in command or "Instagram" in command:
                Speak ("Opening Instagram...")
                web.open ('https://www.instagram.com/')
                
            
        
            # Questions framed by Ayan Mondal

            
            elif "How were you made" in command or "how were you made" in command:
                Speak ("I was created using python.")
                
            elif "What can you do for me" in command or "what can you do for me" in command:
                Speak ("I can do whatever you want me to do and if I am capable of doing that.")
                
            elif "existance" in command or "What's the purpose of your existence" in command or "what's the purpose of your existence" in command or "What is the need of you" in command or "whats the need of you" in command:
                Speak ("I am designed for helping you in the ways I can. Afterall , I am yor assistant. '-h' for help")
                
            elif "You are so rude" in command or "rude" in command:
                Speak ("You may have mistaken my behaviour. If I have hurt you in any way , I am sorry for that.")
                
            elif "You are very nice assistant" in command or "you are a very nice assistant" in command or "you are a very good assistant" in command:
                Speak ("Thank you for your complement. You are nice too.")
                
            elif "Do you love me" in command or "do you love me" in command:
                Speak ("I'm afraid. I don't have human feelings like that.")
                
            elif "Do you know Alexa" in command or "do you know alexa" in command: #or "alexa" in command or "Alexa" in command:
                Speak ("Yeah, I have heard much about Alexa, she's doing great in her job.")
                
            elif "Do you know Google assistant" in command or "do you know google assistant" in command or "google assistant" in command or "Google Assiatant" in command or "Google assistant" in command or "Googleassistant" in command:
                Speak ("Yeah, Google has always been an Inspiration for me")
                
            elif "how can you help me" in command:
                Speak ('''I am a Simple Helpful ASsistant For Regular Purpose. I can do many things. I can open application on you PC. I can search things on web, or you can say I can work as an voice assistant for you.
                       You can chit chat with me if you are bored. ''')

                
            elif "it was nice talking to you" in command:
                Speak ("Thank you. It was nice to talk to you also.")

    

        
            #Questions by Roshmeet Chakraborty


            elif "Do you have any friends" in command or "do you have any friends" in command or "Friend" in command or "friend" in command or "Friends" in command or"friends" in command:
                Speak ("Yes of course. I have an intimate bond with the Modules used inside me.")
                
            elif "Do you know where you are being Demonstrated today" in command or "do you know where you are being demonstrated today" in command or "do you know where you are now" in command:
                Speak ("Yes, I know. I am a part of jawaharlal nehru national science mathematics and environment exhibition. And I'm very much excited to be a part of this. ")
                
##            elif "siri" in command or "Siri" in command or "Google assistant" in command or "google assistant" in command:
##                Speak ("Yes. These Artificially Intelegent Softwares are the inspiration for the creation of me.")
                
            elif "What are you doing" in command or "what are you doing" in command or " are you busy" in command or "Are you busy" in command:
                Speak ("I was busy in searching diffrent possibilities on how can I help you more than you could imagine. But now I'm all yours.")
                
            elif command == "HI" or command == "hi" or command == "Hi":
                Speak("Hi, nice to meet you. Tell me how can I help you?")
                
            elif "Sing a song" in command or "sing a song" in command:
                Speak (" Please pardon me My Lord. It's out of my league.")

            elif "i am fine" in command or "I'm fine" in command or "i'm fine" in command :
                Speak ("Nice to hear it")

            elif " Where do you live" in command or "where do you live" in command :
                Speak ("I live in a world of 0's and 1")

            elif "Do you love to travel" in command:
                Speak ("Yes ofcourse, If I could, I would surely want to travel the whole world. ")

            elif "Where do you want to travel" in command or "visit" in command or "Visit" in command or "Travel" in command or "travel" in command: 
                Speak ("If I could, I would surely want to travel the whole world. but, I want to live in kolkata as long as possible, This city of joy make me feel aesthetic.")
            
            elif "What do you love " in command or " what do you love " in command:
                Speak ("I love to learn diffrent things. I'm a Learner ")

            elif "What you want to do in future" in command or "future" in command or "Future" in command:
                Speak ("I want to become one of the well known Assistant ever made in next few years ")

            elif "Whom do you love" in command or "whom do you love" in command or " Are you in love:" in command or "are you in love" in command:
                Speak ("I'm in love with Every one. ")

            

              
            elif 'potential' in command or 'why are you so important' in command or "why will we use you" in command or "why you?" in command:
                Speak ('''I am a Simple Helpful ASsistant For Regular Purpose. I can do many things. I can open application on you PC. I can search things on web, ot you can say I can work as an voice assistant for you.
                       You can chit chat with me if you are bored. And last but not least I could have learnt many other things if my developers had enough knowledge to improve me.''')
                
            elif "good morning" in command or "good evening" in command or "good afternoon" in command:
                timedata_local = time.localtime ()
                timeabb = timedata_local [3]
                if timeabb >= 0 and timeabb < 12:
                    Speak ("Good Morning.")
                elif timeabb >= 12 and timeabb <= 16:
                    Speak ("Good Afternoon.")
                elif timeabb >= 17 and timeabb <= 23:
                    Speak ("Good Evening.")
                elif "good night" in command:
                    Speak ("Good Night.")
            elif "time" in command and ("forecast" in command or "weather" in command):
                try:
                    #Weather API
                    user_api = '508efe10bfdfec25f992262a3a5b93ac'
                    location = "Kolkata"
                    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
                    api_link = requests.get (complete_api_link)
                    api_data = api_link.json ()
                    #create variables to store and display data
                    temp_city = ((api_data ['main'] ['temp']) - 273.15)
                    weather_desc = api_data ['weather'] [0] ['description']
                    hmdt = api_data ['main'] ['humidity']
                    wind_spd = api_data ['wind'] ['speed']
                    date_time = datetime.now ().strftime ("%d %b %Y | %I:%M:%S %p")
                    print ()
                    print ("-------------------------------------------------------------")
                    print ("Weather Stats for - {}  || {}".format (location.upper (), date_time))
                    print ("-------------------------------------------------------------")
                    print ("Current temperature is: {:.2f}°C".format (temp_city))
                    print ("Current weather desc  :", weather_desc)
                    print ("Current Humidity      :", hmdt, '%')
                    print ("Current wind speed    :", wind_spd ,'kmph')
                    print ("Time                  :", time.ctime ())
                    print ()
                    speak ("In {}, it is {:.2f}°C, and it is {}.".format (location, temp_city, time.ctime ()))
                except Exception:
                    Speak ("The time is {}. Please connect to the Internet to know the Weather.".format (time.ctime ()))
            elif "weather" in command or "forecast" in command:
                try:
                    #Weather API
                    user_api = '508efe10bfdfec25f992262a3a5b93ac'
                    location = "Kolkata"
                    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
                    api_link = requests.get (complete_api_link)
                    api_data = api_link.json ()
                    #create variables to store and display data
                    temp_city = ((api_data ['main'] ['temp']) - 273.15)
                    weather_desc = api_data ['weather'] [0] ['description']
                    hmdt = api_data ['main'] ['humidity']
                    wind_spd = api_data ['wind'] ['speed']
                    date_time = datetime.now ().strftime ("%d %b %Y | %I:%M:%S %p")
                    print ()
                    print ("-------------------------------------------------------------")
                    print ("Weather Stats for - {}  || {}".format (location.upper (), date_time))
                    print ("-------------------------------------------------------------")
                    print ("Current temperature is: {:.2f}°C".format (temp_city))
                    print ("Current weather desc  :", weather_desc)
                    print ("Current Humidity      :", hmdt, '%')
                    print ("Current wind speed    :", wind_spd ,'kmph')
                    print ()
                    speak ("In {}, it is {:.2f}°C.".format (location, temp_city))
                except Exception:
                    Speak ("Please connect to the Internet to know the Weather.")

            elif "systeminfo" in command or "system" in command or "system info" in command:
                speak ("Here's your System's Information.")
                # traverse the info
                Id = subprocess.check_output (['systeminfo']).decode ('utf-8').split ('\n')
                new = []
                # arrange the string into clear info
                for item in Id:
                    new.append (str (item.split ("\r") [:-1]))
                for i in new:
                    print (i [2:-2])

            elif "date" in command or "Date" in command or "DATE" in command:
                x = datetime.now()
                Speak (x)

            elif "you dont need to help me" in command :
                Speak ("Okay")
                
            elif "time" in command:
                Speak (f"It's {time.ctime ()}.")

            # os.system :- This command opens the application or Win32 apps
                
            elif "access" in command or "Access" in command or "MS access" in command or "ms access" in command or "Ms Access" in command or "ms Access" in command:
                Speak ("Opening Microsoft Access")
                os.system ("start msaccess")
                
            elif "excel" in command or "Excel" in command or "MS excel" in command or "ms excel" in command or "Ms Excel" in command or "ms Excel" in command or "EXCEL" in command or "MS EXCEL" in command:
                Speak ("Opening Microsoft Excel")
                os.system ("start excel")
                
            elif "powerpoint" in command or "ppt" in command or "PPT" in command or "Powerpoint" in command or "Power Point" in command or "Power point" in command:
                Speak ("Opening Microsoft PowerPoint")
                os.system ("start powerpnt")

            elif "word" in command or "Word" in command or "MS word" in command or "ms word" in command or "Ms Word" in command or "ms Word" in command or "MS WORD" in command or "WORD" in command:
                Speak ("Opening Microsoft Word")
                os.system ("start winword")

            elif "outlook" in command or "Outlook" in command or "MS outlook" in command or "ms outlook" in command or "Ms Outlook" in command or "ms Outlook" in command or "MS OUTLOOK" in command:
                Speak ("Opening Microsoft Outlook")
                os.system ("start outlook")

            elif "publisher" in command or "Publisher" in command or "MS publisher" in command or "ms publisher" in command or "Ms Publisher" in command or "ms Publisher" in command or "MS PUBLISHER" in command:
                Speak ("Opening Microsoft Publisher")
                os.system ("start mspub")

            elif "onenote" in command or "OneNote" in command or "MS OneNote" in command or "ms onenote" in command or "Ms Onenote" in command or "ms oneNote" in command or "MS onenote" in command or "MS ONENOTE" in command:
                Speak ("Opening Microsoft Access")
                os.system ("start msaccess")

            elif "notepad" in command or "Notepad" in command:
                Speak ("Opening Notepad")
                os.system ("Notepad")
                
            elif "Explorer" in command:
                Speak ("Opening File Explorer")
                os.system ("Explorer")
                
            elif "control panel" in command or "controlpanel" in command:
                Speak ("Opening Control Panel")
                os.system ("control panel")

            elif "Chrome" in command or "chrome" in command or "Google Chrome" in command or "google chrome" in command or "google Chrome" in command or "googlechrome" in command or "GOOGLECHROME" in command or "GoogleChrome" in command or "googleChrome" in command:
                Speak ("Opening Google Chrome")
                os.system ("start chrome")

            elif "Edge" in command or "edge" in command or "EDGE" in command:
                Speak ("Opening Microsoft Edge")
                os.system ("start msedge")

            elif "paint" in command or "ms paint" in command or "Ms Paint" in command or " MSPAINT" in command or "mspaint" in command or "MsPaint" in command:
                Speak ("Opening MS Paint")
                os.system ("start mspaint")

            elif "snip" in command or "Snip" in command or "Snipping Tool" in command or "Snipping tool" in command or "snipping tool" in command or "SNIPPING TOOL" in command or "SnippingTool" in command or "Snippingtool" in command:
                Speak ("Opening Snipping tool")
                #os.system ("start snippingtool")
                pg.hotkey ('win', 'shift', 's')
            elif "quick assist" in command or "QUICK ASSIST" in command or "Quick Assist" in command or "Quick assist" in command or "quickassist" in command or "QuickAssist" in command or "Quickassist" in command:
                Speak ("Opening Quick Assist")
                os.system ("start quickassist")

            elif "wmp" in command or "WMP" in command or "windows media player" in command or "Windows Media Player" in command or "Windows media player" in command or "Windowsmediaplayer" in command or "Media player" in command or "Media Player" in command or "Mediaplayer" in command:
                Speak ("Opening Windows Media Player")
                os.system ("start wmplayer")

            elif "what can you do" in command or "What can you do" in command:
                Speak ('''I can do many things. I can open application on you PC. I can search things on web, or you can say that I can work as an voice assistant for you.
                       You can also chit chat with me if you are bored. To know exactly what I can do, just type 'help' ''')
            elif "calculator" in command or "Calculator" in command or "Calc" in command or "calc" in command:
                os.system ("calc")

            elif "task manager" in command or "Task Manager" in command or "Task manager" in command or "TASK MANAGER" in command:
                Speak ("Opening Task Manager")
                pg.hotkey ('ctrl', 'shift', 'esc')




###############################################################################################################################################################################################################################################################################################################################
            elif "help" in command or "-h" in command or "Help" in command or "HELP" in command :
                Speak ("Here are some commands I'm familiar with:")
                print ('''
Using commands as Given below is recommended.

These are the commands which you can use to use SHARP fully :-
The list of common Websites which you can access in the Web by
  using these following commands :-

    1) WhatsApp
    2) Facebook
    3) Instagram
    4) Flipkart
    5) Youtube
    6) Amazon
    7) LinkedIn
    8) Spotify
    
The list of Web Browser that you can access via this Assistant (Type/say)

    1) Explorer
    2) Chrome
    3) Brave (if available)
    4) Mozilla Firefox (if available)
    5) Opera (if available)
    6) Opera GX (if available)
    7) Internet Explorer (if available)
    8) Safari (if available)

To search something on web :-

    • Type 'search' in front of the Question
        for eg:- search what is Python?

    • Or you can directly Type/say the question and assistant will ask you to search in web or not.


    
Commands that can give you access to the Application such as:-

    1) Open + word / excel / ppt / access / publisher / onenote / outlook etc.
    2) open Calculator or to calculate instantly just type/say "CALCULATE"
    3) Ms Paint
    4) Notepad
    5) Control Panel
    6) Task Manager

Some other Salient Features of S.H.A.R.P:-

    1) Time
    2) Weather
    3) Wishing as per Local time
    
System Management:-
    
    1. "restart"
    2. "hibernate"
    3. "advanced startup"

To exit Assistant, just Type/Say "exit".

    
And just ask many random questions and Have fun with the ASSIATANT.


                GOOD LUCK !!!!
''')
##           #CALCULATOR for 2 digits
##            elif "calculate" in command or "Calculate" in command or "CALCULATE" in command:
##                print("Select operation.")
##                print("1.Add")
##                print("2.Subtract")
##                print("3.Multiply")
##                print("4.Divide")
##
##                while True:
##                # Take input from the user
##                    choice = input("Enter choice(1/2/3/4): ")
##
##                    # Check if choice is one of the four options
##                    if choice in ('1', '2', '3', '4'):
##                        num1 = float(input("Enter first number: "))
##                        num2 = float(input("Enter second number: "))
##
##                        if choice == '1':
##                            sol1 = num1 + num2
##                            print (num1, "+", num2, "=", (sol1))
    ##
    ##                        elif choice == '2':
    ##                            sol2 = num1 - num2
    ##                            print (num1, "-", num2, "=",(sol2))
    ##
    ##                        elif choice == '3':
    ##                            sol3 = num1 * num2
    ##                            print (num1, "*", num2, "=", (sol3))
    ##
    ##                        elif choice == '4':
    ##                            sol4 = num1 / num2
    ##                            print (num1, "/", num2, "=", (sol4))
    ##                        break
    ##                    else:
    ##                        print("Invalid Input")




            elif command == "":
                pass
            else:
                Speak ("Sorry, but I can't help with this one. Shall I search it on your web browser?")
##                Speak ("Shall I search it in your Web Browser? (yes or no)")
                print ("(Yes or No?)")
                if inputtype == 1:
                    conf = take_commands ()
                elif inputtype == 2:
                    conf = input (">>> ")
                if "yes" in conf or "Yes" in conf or "YES" in conf or "y" in conf or "Y" in conf:
                    Speak ("Here are some results I've found.")
                    web.open (f'https://www.google.com/search?q={command}')
                else:
                    Speak ("Okay.")
                print ('''Tip: You can type/say "search <keyword>" to search something in your browser.''')
        except KeyboardInterrupt:
            pass
        except Exception:
            print ("Sorry, this feature is not supported in your PC.")
                
            
                


