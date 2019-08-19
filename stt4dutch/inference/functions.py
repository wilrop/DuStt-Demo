import os
import subprocess

audio_files_folder = 'inference/uploads/'

def handle_uploaded_file(f):  
    with open(audio_files_folder + f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def run_inference(f, model):
    # The command that we need to execute to get the prediction
    audio_path = os.path.abspath(audio_files_folder + f.name)
    command = "deepspeech --model " + model + " --alphabet alphabet.txt --lm lm.binary --trie trie --audio " + audio_path

    # Get the output from the command and add it to the predictions
    output = subprocess.check_output(command, cwd='/Users/willemropke/Documents/BT-projects/Testing', shell=True)
    output = output[:-1]
    return output