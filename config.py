deepspeech = True #Use Mozilla DeepSPeech
google = True #Use Google Cloud API Speech to Text
remove_wav_dir = True

data_dir = './data/'
input_dir = data_dir+'audio_examples/'
google_credentials = data_dir+ 'project_0123.json' #Replace with your json file from:
'''
https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.135125617.-1992684214.1559066420
More info here:
https://cloud.google.com/docs/authentication/production
'''

# These will be created automatically:
wav_dir = input_dir[:-1]+'_wavs/'
deepspeech_models = data_dir+'deepspeech-0.5.0-models/'
output_dir = data_dir+'transcriptions/'

