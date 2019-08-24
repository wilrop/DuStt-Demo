from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .functions import handle_uploaded_file
from .functions import run_inference as specific_inference
from .forms import AudioFile 

import os
from datetime import datetime

path = 'inference/uploads/'

def index(request):
    if request.method == 'POST':  
        audio = AudioFile(request.POST, request.FILES)  
        if audio.is_valid():  
            handle_uploaded_file(request.FILES['file'])    
                      
    audio = AudioFile() 
    audioFiles =  os.listdir(path)
    audioFiles = filter(lambda x: x.endswith(".wav"), audioFiles)
    return render(request, "home.html", {'form':audio, 'audioFiles':audioFiles})

def upload(request):
    filename = datetime.now().strftime("%d-%m-%Y:%H-%M-%S") + ".wav"
    audioFile = request.body

    with open(path + filename, 'wb+') as destination:  
        destination.write(audioFile)

    audio = AudioFile()
    audioFiles =  os.listdir(path)
    audioFiles = filter(lambda x: x.endswith(".wav"), audioFiles)
    return HttpResponse("Klaar")

def run_inference(request):
    model = request.POST.get('model', None)
    audio = request.POST.get('audio', None)

    output = specific_inference(model, audio)
    output = output.decode("utf-8")

    data = {                        
        'output': output,
    }
    return JsonResponse(data)