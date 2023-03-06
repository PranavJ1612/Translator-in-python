import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

#Recognizer class object
recog1 = spr.Recognizer()

#microphone instance
mc= spr.Microphone()

#Capturing Voice
with mc as source:
    print("Speak 'hi bixby' to initialize the Translation !")
    print("```````````````````````````````````````````````````````")
    recog1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog1.listen(source)
    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()

#After 'hi bixby' is recognized then it will recognise it i.e recorder initialized with hello word!
if 'hi bixby' in MyText:

    translator = Translator()     #method for translation
    from_lang = 'en'                    # short form of lang english that u will speak
    to_lang = 'hi'                          # lang in which it is converted

    with mc as source:

        print("Speak a sentence.....")
        recog1.adjust_for_ambient_noise(source, duration=0.2)

        audio = recog1.listen(source)           #Storing the audio into audio variable
        get_sentence = recog1.recognize_google(audio)     # using google method to convert audio into text

        try:
            print("Phase to be Translated : " + get_sentence)               #speech to be translated is printed
            text_to_translate = translator.translate(get_sentence, src = from_lang , dest = to_lang)   #translate method for transaltion of sentece from eng to hin

            text = text_to_translate.text   #translated text stored in text variable

             #use of gTTs-google text to speech , which transalte text into desired lang. And slow=False as by default gTTs speaks very slowly
            speak = gTTS(text=text , lang= to_lang, slow=False)   

            speak.save("captured_voice.mp3")                   #speech saved with save method

            os.system("start captured_voice.mp3")                  #Used os module to run that translated audio

        except spr.UnknownValueError:                             #desired expections to occur
            print("Unable to understand the input")
        
        except spr.RequestError as e:                                   
            print("Unable to provide req. output".format(e))


