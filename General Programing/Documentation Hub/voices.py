text = """
Pytts3  text to speech conversion library.
Offline
Supports TTS engines including Sapi5, nsss, and espeak

"""

import pyttsx3

import pyperclip as pc
text2 = pc.paste().rstrip("\n")

def readtext(text):
    

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

      
    # for voice in voices: 
    #     # to get the info. about various voices in our PC  
    #     print("Voice:") 
    #     print("ID: %s" %voice.id) 
    #     print("Name: %s" %voice.name) 
    #     print("Age: %s" %voice.age) 
    #     print("Gender: %s" %voice.gender) 
    #     print("Languages Known: %s" %voice.languages)

    rate = engine.getProperty('rate')
    


    engine.setProperty('voice', voices[0].id)

    #  Clean ans noramalization
    replacer1 = ['’','‘', '•', '“', '”']
    replacer2 = ['–', "#", "[…]", "→", "_", "—", "", "‐"]
    text = ' '.join(text2.split())
    for i in replacer1:
        text = text.replace(i, '')
    for i in replacer2:
        text = text.replace(i, ' ')
    text = text.replace("XMLHttpRequest", 'XHR ')
    #text = ' '.join(text.splitlines())

    # Say
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    readtext(text2)


