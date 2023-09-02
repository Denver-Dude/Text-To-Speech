import pyttsx3

bot = pyttsx3.init()
voices = bot.getProperty('voices')
def talk(text):
    bot.say(text)
    bot.runAndWait()

def Text():
    print("You can now paste ")
    main_Text =  input()
    print("Generating Audio")
    talk(main_Text)
    s = input("Is it ok?")
    if s == "yes" or s == "Yes":
        print("Your File is saved!")
        bot.save_to_file(main_Text, 'Your_MP3.mp3')
        bot.runAndWait()
        print("please rate us on google meet! lol")
    else:
        print("Sad to hear that, try again!")
        Male_Female()

def Male_Female():
    Voice_Type = input("Who's voice do you want? \n"
                       "[1] Men \n"
                       "[2] Female \n")
    if Voice_Type == "1":
        bot.setProperty('voice', voices[0].id)
        Text()
    elif Voice_Type == "2":
        bot.setProperty('voice', voices[1].id)
        Text()
    else:
        print("Sorry I did not understand, try again")
        Male_Female()



def welcome():
    ask = input("Welcome to AuMa \n"
                "Shall we get started?\n")
    if ask == "Yes" or ask == "yes":
        Male_Female()
    if ask == "No" or ask == "no":
        print("ClosingApp")
        quit()
    else:
        print("i did not understand")
        welcome()
welcome()