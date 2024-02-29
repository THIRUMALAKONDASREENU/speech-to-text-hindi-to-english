pip install pydub
from pydub import AudioSegment

def mp3_to_wav(input_mp3, output_wav):
    audio = AudioSegment.from_mp3(input_mp3)
    audio.export(output_wav, format="wav")


mp3_file_path ="/content/1.mp3"
wav_file_path = "/content/output/1.wav"
mp3_to_wav(mp3_file_path, wav_file_path)


import os
import speech_recognition as sr

from googletrans import Translator



def batch_process_hindi_audio(audio_files):
    recognizer = sr.Recognizer()
    results = {}

    for audio_file in audio_files:
        if not os.path.exists(audio_file):
            print(f"File not found: {audio_file}")
            continue

        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        try:
            
            text = recognizer.recognize_google(audio_data, language="hi")
            results[audio_file] = text
        except sr.UnknownValueError:
            results[audio_file] = "Could not understand audio"
        except sr.RequestError as e:
            results[audio_file] = f"Error with the speech recognition service: {e}"

    return results


audio_files_list = ["/content/output/1.wav"]
results = batch_process_hindi_audio(audio_files_list)

def translate_hindi_to_english(hindi_text):
  translator = Translator()
  translation = translator.translate(hindi_text, src='hi', dest='en')
  return translation.text

for audio_file, result in results.items():
    
    hindi_text = result
    with open(file="/content/result.txt", mode='w') as file:
      file.write(hindi_text)

english_text = translate_hindi_to_english(hindi_text)
print("Hindi Text:", hindi_text)
print("English Translation:", english_text)

from translate import Translator

def translate_hindi_file(input_file, source_lang='hi', target_lang='en'):
    with open(input_file, 'r', encoding='utf-8') as file:
        hindi_text = file.read()

    translator= Translator(to_lang=target_lang, from_lang=source_lang)
    english_text = translator.translate(hindi_text)
    return english_text
    
input_file_path = "/content/result.txt"
translate_hindi_file(input_file_path)


