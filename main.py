from gtts import gTTS
import os

print("Make your text into .mp3 file\n")
mytext = input("Enter the test you want to listen - \n")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("Reading.mp3")

os.system("Reading.mp3")
