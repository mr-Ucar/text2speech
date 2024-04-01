#!/usr/bin/python3
#emreybs & #mr-Ucar

from gtts import gTTS
import os
from time import sleep
import hashlib # For hashing the text to create a unique filename

def get_hashed_filename(text):
    return hashlib.md5(text.encode()).hexdigest() + ".mp3"

def convert_text_to_speech(text, lang='en'):
    try:
        output = gTTS(text=text, lang=lang, slow=False)
        filename = get_hashed_filename(text)
        output.save(filename)
        os.system(f"start {filename}")
        sleep(0.1)
        print(f"\nThe sentence/text you provided has been converted and saved as {filename}:\n\n", text)
    except Exception as e:
        sleep(0.1)
        print(f"An error occurred while converting text to speech: {e}")

def main():
    sleep(0.1)
    print("\n\tWelcome to the Text-to-Speech Converter")
    sleep(0.1)
    print("\t----------------------------------------\n")
    sleep(0.1)
    print("This program converts the text you provide into an audio file in mp3 format.")
    sleep(0.1)
    print("\t----------------------------------------\n")
    sleep(0.1)

    banner = """
    .•♫•♬• Convert TEXT to mp3 •♬•♫•. 
                by mr-Ucar
        """
    print(banner)


    myText = input("\nEnter a sentence or text for me to convert to speech: \n\n")
    sleep(0.1)
    if not myText.strip():
        print("You must enter some text to convert.")
        return

    sleep(0.1)
    myLang = input("\nEnter the language code (e.g., 'en' for English, 'tr' for Turkish, 'fr' for French):\n\n").lower() 
    print("\n")
    print("For better pronunciation, you can use the language code for the language you are using.")
    sleep(0.2)
    print("For example, 'en' for English, 'tr' for Turkish, 'fr' for French, etc.")
    sleep(0.2)
    print("Tip: If you provide an English text but then the language code is 'tr', the pronunciation may not be accurate.\n")
    sleep(0.1)
    if not myLang.strip():
        print("You must enter a language code.\n")
        return

    convert_text_to_speech(myText, myLang)
    sleep(0.1)
    print("\nThank you for using the simple Text-to-Speech Converter. I hope it was helpful.\n")

if __name__ == "__main__":
    main()
