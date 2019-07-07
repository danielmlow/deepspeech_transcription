#!/usr/bin/env python3

'''
Author: Daniel M. Low
https://github.com/danielmlow/transcribe_deepspeech
License: Apache 2.0
'''

import os
import speech_recognition as sr_audio
import config

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return


def to_wav(input_dir = None, filename = None, output_dir = None, output_filename = None, sampling_rate = '16000', bit_rate = '16'):
    mkdir(output_dir)
    os.system(' '.join(['ffmpeg', '-i', input_dir+filename, '-ar', sampling_rate, '-ac', '1',
						'-ab', bit_rate, output_dir+output_filename, '-y']))
    return


def transcribe_google(file):
    # transcribe with google speech API, $0.024/minute 
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(file) as source:
        audio = r.record(source) 
    transcript=r.recognize_google_cloud(audio)
    return transcript 


if __name__ == "__main__":
    # Paths
    input_dir = config.input_dir #./data/wavs_01234/
    wav_dir = config.wav_dir
    model_dir = config.deepspeech_models
    output_dir = config.output_dir
    # Create output dir
    mkdir(output_dir)
    files = os.listdir(input_dir)
    try: files.remove('.DS_Store')
    except: pass
    files.sort()
    for file in files:
        # convert to 16kHz and 16bit wav
        converted_filename = file[:-4]+'_16khz.wav'
        to_wav(input_dir = input_dir, filename=file, output_dir = wav_dir,output_filename=converted_filename,sampling_rate='16000', bit_rate = '16')

        if config.deepspeech:
            command = 'deepspeech --model {0}output_graph.pb --alphabet {0}alphabet.txt --lm {0}lm.binary --trie {0}trie --audio {1} >> {2}'.format(model_dir, wav_dir+converted_filename, output_dir+file[:-4]+'_deepspeech.txt')
            os.system(command)
        if config.google:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.google_credentials
            transcript = transcribe_google(wav_dir+converted_filename)
            with open(output_dir + file[:-4] + '_google.txt', 'a+') as f:
                f.write(transcript)
    if config.remove_wav_dir:
        os.system('rm -r '+config.wav_dir)






