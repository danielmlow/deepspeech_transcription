# Fast setup for using DeepSpeech to transcribe audio files for free -- compare to Google Speech-to-Text

#### Intro

Instead of paying for transcriptions, speech recognition engines have been improved to the point where relatively decent automatic transcriptions can be performed for free. These transcriptions can then be edited by a human annotator if required, which would reduce costs.  

Mozilla, the open-source community that created Firefox, has developed [DeepSpeech](https://github.com/mozilla/DeepSpeech), which is an open source Speech-To-Text engine based on a [Baidu's Deep Speech model](https://arxiv.org/abs/1412.5567). They trained it on CommonVoice corpora, an effective approach to collecting data from the community across many languages (you can quickly contribute  [here](https://voice.mozilla.org/en)). Using the DeepSpeech 0.5.0 model provided below, they achieve 8.22% word error rate on the LibriSpeech clean test corpus. 

Below is an fast setup to use DeepSpeech and the paid alternative Google Cloud Text-to-Speech (with a 300-minute free trial). I have found they perform similarly on certain audio files but Google's engine works considerably better on others (at least for now), although I did not perform any systematic/quantitative comparisons. It's a matter of trying it out on your audio files and perhaps preprocessing preprocessing them in different ways to try to improve performance.  

#### Setup
[Install python3](https://realpython.com/installing-python/)

Open the terminal and run these commands:

```
git clone https://github.com/danielmlow/deepspeech_transcription.git
cd transcribe_deepspeech
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```
Download pre-trained DeepSpeech model into `./data/` directory (1.9 GHz). If downloaded into other directory, change path in last parameter. New model paths can be obtained [here](https://github.com/mozilla/DeepSpeech/releases). 

```
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.5.0/deepspeech-0.5.0-models.tar.gz -P data/
tar xvfz data/deepspeech-0.5.0-models.tar.gz # Unzips
rm data/deepspeech-0.5.0-models.tar.gz
```

This will output ./data/deepspeech-0.5.0-models/ directory. 

Choose if you want to run DeepSpeech Google Cloud Speech-to-Text or both by setting parameters in config.py

To use Google Cloud API, obtain credentials here (1-year $300 free credit):
https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.135125617.-1992684214.1559066420
More info here: 
https://cloud.google.com/docs/authentication/production

Set paths in config.py. Beyond the data and input directories with audio files which you must place and set paths to, it will create all other directories that do not exist already.

It will convert all audio files to 16kHz and 16 bit wav files into a temporary wav_dir, required by DeepSpeech. 


Run:
```transcribe.py```


More info:
[https://github.com/mozilla/DeepSpeech](https://github.com/mozilla/DeepSpeech)


#### Example audio files ground-truth transcription

8455-210777-0068.wav:   "Your power is sufficient I said"

4507-16021-0012.wav:     "Why should one halt on the way?"

2830-3980-0043.wav:       "Experience proves this"


#### DeepSpeech transcription
your power is sufficient i said

why should one halt on the way

*experience proof this

#### Compare to Google Cloud Speech-to-Text transcription
your power is sufficient I said

why should one halt on the way

experience proves this




