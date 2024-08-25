import googletrans
import speech_recognition
import speech_recognition as sr
import gtts
import playsound

recognizer = speech_recognition.Recognizer()
with sr.Microphone() as source:
    print("Speek Now :")
    voice = recognizer.listen(source)
    listen = recognizer.recognize_google(voice,language="en")
    print(listen)
translator = googletrans.Translator()
translate = translator.translate(listen,dest="hi")
print(translate.text)
converted_audio = gtts.gTTS(translate.text,lang="hi")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")