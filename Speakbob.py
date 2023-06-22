# importing module
import win32com.client

print("Welcome to Speakob 1.1 Created By Coded Bhai")

# creating an speaker object using win32com module
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# creating loop for module
while True:
    # taking input from user what user wants to listen
    statement = input("Enter what you want to listen from me: ")
    # giving an if statement for while loop to break
    if statement == "-":
        speaker.Speak("Thanks for using me")
        break
    # to speak what iss input
    speaker.Speak(statement)
