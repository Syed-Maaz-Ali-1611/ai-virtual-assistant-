#============================ IMPORTING IMPORTANT LINRARIES =====================================


import customtkinter
from tkinter import *    
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr 
import datetime as datetime
import webbrowser
import os
import smtplib as smtplib
import pyjokes
import time
from tkinter import *
from PIL import ImageTk,Image
import tkvideo


#============================VOICE RECOGNTION SYSTEM =====================================
def english():
    def voice_eng():
        engine = pyttsx3.init('sapi5') 
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices [1].id)
        time.sleep(3) 

        def speak(audio): 
            engine.say (audio) 
            engine.runAndWait()
            time.sleep(2) 

        def wish() : 
                    time = int (datetime.datetime.now().hour) 
                    if time >= 0 and time < 12: 
                        speak ("Good Morning!") 
                    elif time >= 12 and time < 18: 
                        speak ("Good Afternoon!") 
                    else: 
                        speak ("Good Evening!") 
                    
                    speak("say password to open up Hawa") 
        wish() 
        time.sleep(1)


    #================================= VOICE LOCK INITIAILIZATION ===================================


        def locker_eng():
                        r = sr. Recognizer() 

                        with sr.Microphone () as source: 
                            
                            r.pause_threshold = 1
                            audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            
                            try: 
                                speak ("Recognizing...") 
                                password = r.recognize_google (audio, language='en-in') 
                                speak (f"You said: {password} \n") 

                                if password == "Salam":
                                    speak("My greetings to you too")
                                    voice_assistant_eng()
                                    
                                else:
                                    print("wrong password")
                                    messagebox.showerror("Enter correct user name and password")

                            except sr.UnknownValueError: 
                                print ("Would you mind repeating that?") 
        locker_eng()     


    #===============================SETTING THE TRANSLATOR=========================================

    # from googletrans import Translator
    # from gtts import gTTS
    # import os 
    # translator = Translator()


    # def talk(urdu_talk):
    #     translated_text = translator.translate(urdu_talk, src='en', dest = 'ur')
    #     speech = gTTS(translated_text.text, lang = 'ur', slow = False)
    #     speech.save("hava.mp3")
    #     os.system("start hava.mp3")
    #     time.sleep(3)
        
    #==========================================Voice Assistant======================================


    def voice_assistant_eng():
            
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")



        root = customtkinter.CTk()
        root.geometry("400x200")
        # root.place(x=500, y=500)
        frame = customtkinter.CTkFrame(master= root)
        frame.pack(pady = 20, padx = 60 , fill = "both", expand = True)
        label = customtkinter.CTkLabel(master= frame , text= "Next Gen AI Virtual Assistant")
        label.pack(pady = 12 , padx = 10)
        # video = tkvideo.Video(label)
        # # video.pack()
        # # video.play("freq.mp4")
        assistant_button = customtkinter.CTkButton(master=frame, text= "HAWAA" , command= audio_eng, fg_color= "#109e57" , hover_color="#13d675")
        assistant_button.pack(pady= 12, padx = 10)
        root.mainloop()


    #======================================TTS & MICROPHONE========================================

    def audio_eng():
        engine = pyttsx3.init('sapi5') 
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices [1].id) 

        def speak(audio): 
            engine.say (audio) 
            engine.runAndWait() 
        

        def takeCommand_eng(): 
                r = sr. Recognizer() 
                
                with sr.Microphone () as source:
                    speak("hawa here, How can i help you") 
                    speak("say something") 
                    
                    r.pause_threshold = 1
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    
                try: 
                    print ("Recognizing...") 
                    query = r.recognize_google (audio, language='en-in') 
                    speak (f"You said: {query} \n") 
                
                except Exception as e: 
                    speak ("Would you mind repeating that?") 
                    return "None" 
                return query 

        #====================================COMMANDS============================================

        from datetime import datetime

        while True: 
                query = takeCommand_eng().lower() 
                    
                if 'open youtube' in query:
                    speak("opening youtube")
                    quit() 

                elif 'open google' in query:
                    speak("sir, what should i search on google")
                    webbrowser.open("google.com")
                    cm = takeCommand_eng().lower()
                    webbrowser.open(f"{cm}")
                    quit()
                
                elif 'open WhatsApp' in query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif 'thank you' in query: 
                        speak ("aww my pleasure") 
                        
                elif 'play my favourite video' in query: 
                        speak ("PLAYING NOW") 
                        webbrowser.open("https://www.youtube.com/watch?v=HTHj_pvEYYE") 
                        quit()


                elif 'sing a song' in query: 
                        speak ("PLAYING NOW") 
                        webbrowser.open("https://www.youtube.com/shorts/44dXTroE1RI") 
                        quit()

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")

                elif 'open facebook' in query:
                    webbrowser.open("facebook.com")

                elif "jokes" in query or "joke" in query:
                    speak(pyjokes.get_joke())

                elif "are you single" in query:
                    speak("""No i am married i have one husband and two childerns name J V and J S""")

                elif "can i see your face" in query:
                    speak("no sir actual i have pimples on my face so i cant show may face")
                    time.sleep(3)

                elif "should we go for a date" in query or "can i date you" in query:
                    speak("""sir please dont flirt with me i am married if you ask again i complain to my husband""")
                    time.sleep(3)

                elif "quality of hawa" in query or "qualities of hawa" in query:
                    speak("""oh you wanna know about my husband quality well... first he is my husband secondly 
                    he has many good quality like he has a friendly service , strong and protective nature and many more""")
                    time.sleep(3)

                elif "bad quality of hawa" in query or "bad qualities of hawa" in query:
                    speak("""well my husband is so busy and arrogant """)
                    time.sleep(3)

                elif 'play music' in query:
                    music_dir = 'E:\\For ai\\music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    quit()

                elif 'play movie' in query:
                    movie_dir = 'E:\\For ai\\movie'
                    movie = os.listdir(movie_dir)
                    print(movie)
                    os.startfile(os.path.join(movie_dir, movie[0]))
                    quit()

                elif 'open code' in query or 'open vs code' in query:
                    codePath = "C:\\Users\\Adil Abbas Khuhro\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath) 
                    time.sleep(3)           

                elif 'open MS word' in query or 'open word' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'open MS Excel' in query or 'open excel' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
                    os.startfile(codePath)
                
                elif 'open MS Power Point' in query or 'open power point' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
                    os.startfile(codePath)
                    time.sleep(3)
                
                elif 'open MS Access' in query or 'open access' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access"
                    os.startfile(codePath)
                    time.sleep(3)
                
                elif 'open MS Outlook' in query or 'open outlook' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'open MS Publisher' in query or 'open publisher' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Publisher"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%I:%p")
                    speak(f"Sir, the time is {strTime}")
                    time.sleep(3)

                elif 'tell me the day' in query or 'what the day today' in query:
                    strTime = datetime.datetime.now().strftime("%A")
                    speak(f"Sir, today is {strTime}")
                    time.sleep(3)
                
                elif 'open my soundcloud playlist' in query: 
                        speak ("PLAYING NOW") 
                        webbrowser.open("https://soundcloud.com/discover/sets/charts-top:all-music:pk?si=e0ba926d0a2c4ece8c62c904404c8264&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
                        quit()

                elif 'open my gmail' in query or 'gmail' in query:
                        speak("Opening your id !!")
                        webbrowser.open("https://mail.google.com/mail/")
                        quit()  
                
                elif "my today's schedule" in query or 'schedule' in query:

                    import datetime as datetime
                    if datetime.datetime.now().strftime("%A") == "Monday":
                        speak(""" ON MONDAY,
                    YOU HAVE ON CAMPUS SCD LAB FROM 8:30AM TO 11:30AM 
                    AND THEN FROM
                    11:30AM TO 1PM YOU HAVE SCD HEORY CLASS
                    AND THEN FROM
                    1PM TO 2:30PM YOU HAVE HCI CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP 
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Tuesday":
                        speak(""" ON TUESDAY
                    YOU HAVE ON CAMPUS CLASSE OF AI  FROM 8:30AM TO 10AM 
                    AND THEN FROM
                    10AM TO 11:30AM YOU HAVE CCN THEORY CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Wednesday":
                        speak(""" ON WEDNESDAY
                    YOU HAVE ON CAMPUS CLASSE OF AI  FROM 8:30AM TO 10AM 
                    AND THEN FROM
                    10AM TO 11:30AM YOU HAVE HCI THEORY CLASS
                    AND THEN FROM
                    11:30AM TO 1PM YOU HAVE CCN THEORY CLASS
                    AND THEN FROM
                    1PM T 2:30PM YOU HAVE EE CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Thursday":
                        speak(""" ON THURSDAY
                        YOU HAVE ON CAMPUS LAB OF AI FROM 11:30AM TO 2:30PM 
                        AND THEN FROM
                    2:30PM TO 5:30PM YOU HAVE CCN LAB
                    AND THEN FROM
                    6PM TO 7PM YOU HAVE TO ATTEND AN ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Friday":
                        speak(""" ON FRIDAY
                        YOUR HAVE YOUR ON CAMPUS CLASSE OF EE FROM 2:30PM TO 4PM 
                    AND THEN FROM
                    4PM TO 5:30PM YOU HAVE SCD THEORY CLASS
                    AND THEN FROM
                    6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Saturday":
                        speak("""
                        THIS IS YOUR WEEKEND DO ONLY NECESSARY WORK OTHERWISE CHILL AND HAVE SOME GOOD TIME WITH YOUER FRIENDS AND FAMILY.
                        IF THERE WILL BE ANY NECESSARY WORK TO THEN I WILL REMIND YOU DONT WORRY.
                    """)
                        
                    
                    elif datetime.datetime.now().strftime("%A") == "Sunday":
                        speak("""
                        THIS IS YOUR WEEKEND DO ONLY NECESSARY WORK OTHERWISE CHILL AND HAVE SOME GOOD TIME WITH YOUER FRIENDS AND FAMILY.
                        IF THERE WILL BE ANY NECESSARY WORK TO THEN I WILL REMIND YOU DONT WORRY.
                    """)
                    time.sleep(38)

                elif 'send email' in query:
                        try:
                            speak("To whom should I send the email?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            recipient = r.recognize_google(audio, language='en-in')
                            speak(f"What should the subject of the email be?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            subject = r.recognize_google(audio, language='en-in')
                            speak("What is the message that you would like to send?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            message = r.recognize_google(audio, language='en-in')
                            speak("Sending email...")
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login("adilabbbaskhuhro@gmail.com", "!ns@niyaT_Zindabad")
                            msg = f"Subject: {subject}\n\n{message}"
                            server.sendmail("ms7924456khas@gmail.com", recipient, msg)
                            server.quit()
                            speak("Email has been sent.")
                        except Exception as e:
                            speak("Sorry, I was unable to send the email. Error: " + str(e))
                        time.sleep(18)

                elif 'allah hafiz'in query or 'bye' in query: 
                        speak ("Bye . See you soon") 
                        quit()
                else:
                    speak("Sorry, I am not programmed to do that yet.")
                    time.sleep(3)
        

    #============================ MANNUAL LOGIN INITIALIZATION =====================================


    def login():
        username = "123"
        password = "123"
        username_login = username_entry.get()
        password_login = password_entry.get()  
        if (username_login == "" and password_login == ""):
            messagebox.showwarning(title= "Error", message= "Enter your user name and password")
        elif(username_login == username and password_login == password):
            voice_assistant_eng()
        elif(username_login != username and password_login != password):
            messagebox.showwarning(title= "Error", message= "Wrong user name and password")



    #============================ CREATING THE MAIN LOGIN WINDOW =====================================


    def main_window_eng():
        global username_entry
        global password_entry
        global Login_button


        window = Tk()
        window.geometry('1350x850')
        window.resizable(100, 100)
        window.title('Login Page')

                    # ========================================================================
                    # ============================background image============================
                    # ========================================================================
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(window, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')
                    # ====== Login Frame =========================
        lgn_frame = Frame(window, bg='black', width=950, height=600)
        lgn_frame.place(x=200, y=70)
                    
                    # ====== voice unlock Frame =========================
        voice_frame = Frame(window, bg='#050505', width=350, height=60)
        voice_frame.place(x=740, y=579)

                    # ========================================================================
                    # ========================================================
                    # ========================================================================
        txt1 = "Welcome to Next"
        heading = Label(lgn_frame, text =txt1, 
                        font=('yu gothic ui', 22, "bold"), 
                        bg="#040405",
                        fg='white',
                        bd=5,
                        relief=FLAT)
        heading.place(x=80, y=25, width=350, height=30)


        txt2 = "Gen A.I Virtual Assistant"
        heading = Label(
                lgn_frame, 
                        text =txt2, 
                        font=('yu gothic ui', 22, "bold"), 
                        bg="#040405",
                        fg='white',
                        bd=5,
                        relief=FLAT)
        heading.place(x=80, y=55, width=350, height=30)

                    # ========================================================================
                    # ============ Left Side Image ================================================
                    # ========================================================================
        side_image = Image.open('images\\siri2.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='#040405')
        side_image_label.image = photo
        side_image_label.place(x=5, y=100)

                    # ========================================================================
                    # ============ Sign In Image =============================================
                    # ========================================================================
        sign_in_image = Image.open('images\\hyy (2).png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=645, y=25)

                    # ========================================================================
                    # ============ Sign In label =============================================
                    # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=660, y=140)

                    # ========================================================================
                    # ============================username====================================
                    # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="#040405", fg="#bfe0f5",
                                                font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=180)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#050505", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        username_entry.place(x=580, y=217, width=244)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=550, y=240)
                    # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=213)

                    # ========================================================================
                    # ============================login button================================
                    # ========================================================================
        lgn_button = Image.open('images\\btn.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=340)
        login_btn = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#06b2ff', cursor='hand2', activebackground='#0aa0fc', fg='white', command=login)
        login_btn.place(x=20, y=10)

        Login_button = login_btn

                    # ========================================================================
                    # ============================voice lock button================================
                    # ========================================================================
        voice_button = Image.open('images\\btn.png')
        photo = ImageTk.PhotoImage(lgn_button)
        voice_button_label = Label(window, image=photo, bg='#040405')
        voice_button_label.image = photo
        voice_button_label.place(x=760, y=580)
        voi = Button(window, text='Voice Unlock', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                        bg='#06b2ff', cursor='hand2', activebackground='#0aa0fc', fg='white', command= voice_eng)
        voi.place(x=780, y=590)

                    # ========================================================================
                    # ============ voice unlock label =============================================
                    # ========================================================================
        voice_label = Label(
                    window, 
                    text="Unlock assistant through voice", 
                    bg="#040405", fg="white",
                    font=("yu gothic ui", 17, "bold")
                    )
        voice_label.place(x=740, y=525)
                    

                    # ========================================================================
                    # ============================password====================================
                    # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="#040405", fg="#bfe0f5",
                                                font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=270)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#050505", fg="#6b6a69",
                                                font=("yu gothic ui", 12, "bold"), show="*")
        password_entry.place(x=580, y=305, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=330)
                    # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=303)
                    # ========= show/hide password ==================================================================
        show_image = ImageTk.PhotoImage \
                        (file='images\\show.png')

        hide_image = ImageTk.PhotoImage \
                        (file='images\\hide.png')


        def show_eng():
                
                    hide_button = Button(lgn_frame, image=  hide_image, command = hide_eng, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
                    
                    hide_button.place(x=820, y=305)
                    password_entry.config(show='')
        def hide_eng():
                    show_button = Button(lgn_frame, image = show_image, command = show_eng, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
                    show_button.place(x=820, y=305)
                    password_entry.config(show='*')



        show_button = Button(lgn_frame, image=show_image, command=show_eng, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=820, y=305)
        window.mainloop()
    main_window_eng()

english()




#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#=====================================================URDU CODEE====================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================




def urdu():


    #============================VOICE RECOGNTION SYSTEM =====================================

    def voice():
        engine = pyttsx3.init('sapi5') 
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices [1].id)
        time.sleep(3) 

        def speak(audio): 
            engine.say (audio) 
            engine.runAndWait()
            time.sleep(2) 

        def wish() : 
                    time = int (datetime.datetime.now().hour) 
                    if time >= 0 and time < 12: 
                        talk ("Good Morning!") 
                    elif time >= 12 and time < 18: 
                        talk ("Good Afternoon!") 
                    else: 
                        talk ("Good Evening!") 
                    
                    talk("say password to open up Hawa") 
        wish() 
        time.sleep(1)


    #================================= VOICE LOCK INITIAILIZATION ===================================


        def locker():
                        r = sr. Recognizer() 

                        with sr.Microphone () as source: 
                            
                            r.pause_threshold = 1
                            audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            
                            try: 
                                talk ("Recognizing...") 
                                password = r.recognize_google (audio, language='en-in') 
                                talk (f"You said: {password} \n") 

                                if password == "Salam":
                                    talk("My greetings to you too")
                                    voice_assistant()
                                    
                                else:
                                    print("wrong password")
                                    messagebox.showerror("Enter correct user name and password")

                            except sr.UnknownValueError: 
                                print ("Would you mind repeating that?") 
        locker()     


    #===============================SETTING THE TRANSLATOR=========================================

    from googletrans import Translator
    from gtts import gTTS
    import os 
    translator = Translator()


    def talk(urdu_talk):
        translated_text = translator.translate(urdu_talk, src='en', dest = 'ur')
        speech = gTTS(translated_text.text, lang = 'ur', slow = False)
        speech.save("hava.mp3")
        os.system("start hava.mp3")
        time.sleep(3)
        
    #==========================================Voice Assistant======================================


    def voice_assistant():
            
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")



        root = customtkinter.CTk()
        root.geometry("400x200")
        # root.place(x=500, y=500)
        frame = customtkinter.CTkFrame(master= root)
        frame.pack(pady = 20, padx = 60 , fill = "both", expand = True)
        label = customtkinter.CTkLabel(master= frame , text= "Next Gen AI Virtual Assistant")
        label.pack(pady = 12 , padx = 10)
        # video = tkvideo.Video(label)
        # # video.pack()
        # # video.play("freq.mp4")
        assistant_button = customtkinter.CTkButton(master=frame, text= "HAWAA" , command= audio, fg_color= "#109e57" , hover_color="#13d675")
        assistant_button.pack(pady= 12, padx = 10)
        root.mainloop()


    #======================================TTS & MICROPHONE========================================

    def audio():
        engine = pyttsx3.init('sapi5') 
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices [1].id) 

        def speak(audio): 
            engine.say (audio) 
            engine.runAndWait() 
        

        def takeCommand(): 
                r = sr. Recognizer() 
                
                with sr.Microphone () as source:
                    talk("hawa here, How can i help you") 
                    talk("say something") 
                    
                    r.pause_threshold = 1
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    
                try: 
                    print ("Recognizing...") 
                    query = r.recognize_google (audio, language='en-in') 
                    talk (f"You said: {query} \n") 
                
                except Exception as e: 
                    talk ("Would you mind repeating that?") 
                    return "None" 
                return query 

        #====================================COMMANDS============================================

        from datetime import datetime

        while True: 
                query = takeCommand().lower() 
                    
                if 'youtube kholo' in query:
                    talk("opening youtube")
                    quit() 

                elif 'google kholo' in query:
                    talk("sir, what should i search on google")
                    webbrowser.open("google.com")
                    cm = takeCommand().lower()
                    webbrowser.open(f"{cm}")
                    quit()
                
                elif 'WhatsApp kholo' in query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif 'shukrya' in query: 
                        talk ("aww my pleasure") 
                        
                elif 'meri favorite video chalao' in query: 
                        talk ("PLAYING NOW") 
                        webbrowser.open("https://www.youtube.com/watch?v=HTHj_pvEYYE") 
                        quit()


                elif 'gaana sunaao' in query: 
                        talk ("PLAYING NOW") 
                        webbrowser.open("https://www.youtube.com/shorts/44dXTroE1RI") 
                        quit()

                elif 'stackoverflow kholo' in query:
                    webbrowser.open("stackoverflow.com")

                elif 'facebook kholo' in query:
                    webbrowser.open("facebook.com")

                elif "jokes" in query or "joke" in query:
                    talk(pyjokes.get_joke())

                elif 'music kholo' in query:
                    talk ("Aaap ko konsi app pr gana sunna hai ?")
                    
                    def song_app():
                        r = sr. Recognizer() 

                        with sr.Microphone () as source: 
                            
                            r.pause_threshold = 1
                            audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            
                            try: 
                                talk ("Recognizing...") 
                                app_song = r.recognize_google (audio, language='en-in') 
                                talk (f"You said: {app_song} \n") 

                                if app_song == "soundcloud":
                                    talk("Sound cloud khul rha hai .. ")
                                    webbrowser.open("soundcloud.com")
                                elif app_song == "spotify.com":
                                    talk("Spotify khul rha hai...")
                                    webbrowser.open("soptify.com")
                                else:
                                    print("wrong password")
                                    messagebox.showerror("Enter correct user name and password")

                            except sr.UnknownValueError: 
                                print ("Would you mind repeating that?") 
                        song_app()

                elif 'movie kholo' in query:
                    movie_dir = 'E:\\For ai\\movie'
                    movie = os.listdir(movie_dir)
                    print(movie)
                    os.startfile(os.path.join(movie_dir, movie[0]))
                    quit()

                elif 'code kholo' in query or 'vs code kholo' in query:
                    codePath = "C:\\Users\\Adil Abbas Khuhro\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath) 
                    time.sleep(3)           

                elif 'MS word kholo' in query or 'word kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'MS Excel kholo' in query or 'excel kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
                    os.startfile(codePath)
                
                elif 'MS Power Point kholo' in query or 'power point kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
                    os.startfile(codePath)
                    time.sleep(3)
                
                elif 'open MS Access' in query or 'access kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access"
                    os.startfile(codePath)
                    time.sleep(3)
                
                elif 'MS Outlook kholo' in query or 'outlook kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'MS Publisher kholo' in query or 'publisher kholo' in query:
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Publisher"
                    os.startfile(codePath)
                    time.sleep(3)

                elif 'time btao' in query:
                    strTime = datetime.datetime.now().strftime("%I:%p")
                    talk(f"Sir, the time is {strTime}")
                    time.sleep(3)

                elif 'Din btao' in query or 'Ajj kia din hai?' in query:
                    strTime = datetime.datetime.now().strftime("%A")
                    talk(f"Sir, today is {strTime}")
                    time.sleep(3)
                
                elif 'soundcloud playlist kholo' in query: 
                        talk ("PLAYING NOW") 
                        webbrowser.open("https://soundcloud.com/discover/sets/charts-top:all-music:pk?si=e0ba926d0a2c4ece8c62c904404c8264&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
                        quit()

                elif 'gmail' in query or 'gmail kholo' in query:
                        talk("Opening your id !!")
                        webbrowser.open("https://mail.google.com/mail/")
                        quit()  
                
                elif "ajj ka schedule" in query or 'schedule' in query:

                    import datetime as datetime
                    if datetime.datetime.now().strftime("%A") == "Monday":
                        talk(""" ON MONDAY,
                    YOU HAVE ON CAMPUS SCD LAB FROM 8:30AM TO 11:30AM 
                    AND THEN FROM
                    11:30AM TO 1PM YOU HAVE SCD HEORY CLASS
                    AND THEN FROM
                    1PM TO 2:30PM YOU HAVE HCI CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP 
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Tuesday":
                        talk(""" ON TUESDAY
                    YOU HAVE ON CAMPUS CLASSE OF AI  FROM 8:30AM TO 10AM 
                    AND THEN FROM
                    10AM TO 11:30AM YOU HAVE CCN THEORY CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Wednesday":
                        talk(""" ON WEDNESDAY
                    YOU HAVE ON CAMPUS CLASSE OF AI  FROM 8:30AM TO 10AM 
                    AND THEN FROM
                    10AM TO 11:30AM YOU HAVE HCI THEORY CLASS
                    AND THEN FROM
                    11:30AM TO 1PM YOU HAVE CCN THEORY CLASS
                    AND THEN FROM
                    1PM T 2:30PM YOU HAVE EE CLASS
                    AND THEN FROM
                    4PM TO 6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Thursday":
                        talk(""" ON THURSDAY
                        YOU HAVE ON CAMPUS LAB OF AI FROM 11:30AM TO 2:30PM 
                        AND THEN FROM
                    2:30PM TO 5:30PM YOU HAVE CCN LAB
                    AND THEN FROM
                    6PM TO 7PM YOU HAVE TO ATTEND AN ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Friday":
                        talk(""" ON FRIDAY
                        YOUR HAVE YOUR ON CAMPUS CLASSE OF EE FROM 2:30PM TO 4PM 
                    AND THEN FROM
                    4PM TO 5:30PM YOU HAVE SCD THEORY CLASS
                    AND THEN FROM
                    6PM YOU HAVE TO ATTEND ONLINE SESSION
                    AND THEN FROM
                    8PM TO 10PM	YOU HAVE TO COMPLETE YOUR UNIVERSITY ASSINGMENTS
                    AND THEN FROM
                    10PM TO 11PM YOU HAVE TO UPGRADE ME
                    AND THEN 
                    GO TO SLEEP
                    """)
                    elif datetime.datetime.now().strftime("%A") == "Saturday":
                        talk("""
                        THIS IS YOUR WEEKEND DO ONLY NECESSARY WORK OTHERWISE CHILL AND HAVE SOME GOOD TIME WITH YOUER FRIENDS AND FAMILY.
                        IF THERE WILL BE ANY NECESSARY WORK TO THEN I WILL REMIND YOU DONT WORRY.
                    """)
                        
                    
                    elif datetime.datetime.now().strftime("%A") == "Sunday":
                        talk("""
                        THIS IS YOUR WEEKEND DO ONLY NECESSARY WORK OTHERWISE CHILL AND HAVE SOME GOOD TIME WITH YOUER FRIENDS AND FAMILY.
                        IF THERE WILL BE ANY NECESSARY WORK TO THEN I WILL REMIND YOU DONT WORRY.
                    """)
                    time.sleep(38)

                elif 'email bhejo' in query:
                        try:
                            talk("To whom should I send the email?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            recipient = r.recognize_google(audio, language='en-in')
                            talk(f"What should the subject of the email be?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            subject = r.recognize_google(audio, language='en-in')
                            talk("What is the message that you would like to send?")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                r.pause_threshold = 1
                                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            message = r.recognize_google(audio, language='en-in')
                            talk("Sending email...")
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login("adilabbbaskhuhro@gmail.com", "!ns@niyaT_Zindabad")
                            msg = f"Subject: {subject}\n\n{message}"
                            server.sendmail("ms7924456khas@gmail.com", recipient, msg)
                            server.quit()
                            talk("Email has been sent.")
                        except Exception as e:
                            talk("Sorry, I was unable to send the email. Error: " + str(e))
                        time.sleep(18)

                elif 'allah hafiz'in query or 'bye' in query: 
                        talk ("Bye . See you soon") 
                        quit()
                else:
                    talk("Sorry, I am not programmed to do that yet.")
                    time.sleep(3)
        

    #============================ MANNUAL LOGIN INITIALIZATION =====================================


    def login():
        username = "123"
        password = "123"
        username_login = username_entry.get()
        password_login = password_entry.get()  
        if (username_login == "" and password_login == ""):
            messagebox.showwarning(title= "Error", message= "Enter your user name and password")
        elif(username_login == username and password_login == password):
            voice_assistant()
        elif(username_login != username and password_login != password):
            messagebox.showwarning(title= "Error", message= "Wrong user name and password")



    #============================ CREATING THE MAIN LOGIN WINDOW =====================================


    def main_window():
        global username_entry
        global password_entry
        global Login_button


        window = Tk()
        window.geometry('1350x850')
        window.resizable(100, 100)
        window.title('Login Page')

                    # ========================================================================
                    # ============================background image============================
                    # ========================================================================
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(window, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')
                    # ====== Login Frame =========================
        lgn_frame = Frame(window, bg='black', width=950, height=600)
        lgn_frame.place(x=200, y=70)
                    
                    # ====== voice unlock Frame =========================
        voice_frame = Frame(window, bg='#050505', width=350, height=60)
        voice_frame.place(x=740, y=579)

                    # ========================================================================
                    # ========================================================
                    # ========================================================================
        txt1 = "Welcome to Next"
        heading = Label(lgn_frame, text =txt1, 
                        font=('yu gothic ui', 22, "bold"), 
                        bg="#040405",
                        fg='white',
                        bd=5,
                        relief=FLAT)
        heading.place(x=80, y=25, width=350, height=30)


        txt2 = "Gen A.I Virtual Assistant"
        heading = Label(
                lgn_frame, 
                        text =txt2, 
                        font=('yu gothic ui', 22, "bold"), 
                        bg="#040405",
                        fg='white',
                        bd=5,
                        relief=FLAT)
        heading.place(x=80, y=55, width=350, height=30)

                    # ========================================================================
                    # ============ Left Side Image ================================================
                    # ========================================================================
        side_image = Image.open('images\\siri2.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='#040405')
        side_image_label.image = photo
        side_image_label.place(x=5, y=100)

                    # ========================================================================
                    # ============ Sign In Image =============================================
                    # ========================================================================
        sign_in_image = Image.open('images\\hyy (2).png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=645, y=25)

                    # ========================================================================
                    # ============ Sign In label =============================================
                    # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=660, y=140)

                    # ========================================================================
                    # ============================username====================================
                    # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="#040405", fg="#bfe0f5",
                                                font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=180)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#050505", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        username_entry.place(x=580, y=217, width=244)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=550, y=240)
                    # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=213)

                    # ========================================================================
                    # ============================login button================================
                    # ========================================================================
        lgn_button = Image.open('images\\btn.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=340)
        login_btn = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#06b2ff', cursor='hand2', activebackground='#0aa0fc', fg='white', command=login)
        login_btn.place(x=20, y=10)

        Login_button = login_btn

                    # ========================================================================
                    # ============================voice lock button================================
                    # ========================================================================
        voice_button = Image.open('images\\btn.png')
        photo = ImageTk.PhotoImage(lgn_button)
        voice_button_label = Label(window, image=photo, bg='#040405')
        voice_button_label.image = photo
        voice_button_label.place(x=760, y=580)
        voi = Button(window, text='Voice Unlock', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                        bg='#06b2ff', cursor='hand2', activebackground='#0aa0fc', fg='white', command= voice)
        voi.place(x=780, y=590)

                    # ========================================================================
                    # ============ voice unlock label =============================================
                    # ========================================================================
        voice_label = Label(
                    window, 
                    text="Unlock assistant through voice", 
                    bg="#040405", fg="white",
                    font=("yu gothic ui", 17, "bold")
                    )
        voice_label.place(x=740, y=525)
                    

                    # ========================================================================
                    # ============================password====================================
                    # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="#040405", fg="#bfe0f5",
                                                font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=270)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#050505", fg="#6b6a69",
                                                font=("yu gothic ui", 12, "bold"), show="*")
        password_entry.place(x=580, y=305, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=330)
                    # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=303)
                    # ========= show/hide password ==================================================================
        show_image = ImageTk.PhotoImage \
                        (file='images\\show.png')

        hide_image = ImageTk.PhotoImage \
                        (file='images\\hide.png')


        def show():
                
                    hide_button = Button(lgn_frame, image=  hide_image, command = hide, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
                    
                    hide_button.place(x=820, y=305)
                    password_entry.config(show='')
        def hide():
                    show_button = Button(lgn_frame, image = show_image, command = show, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
                    show_button.place(x=820, y=305)
                    password_entry.config(show='*')



        show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                            activebackground="white"
                                            , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=820, y=305)
        window.mainloop()

    main_window()




urdu()