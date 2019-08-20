from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .functions import handle_uploaded_file
from .functions import run_inference as specific_inference
from .forms import AudioFile 

import os
path = 'inference/uploads/'

def index(request):
    if request.method == 'POST':  
        audio = AudioFile(request.POST, request.FILES)  
        if audio.is_valid():  
            handle_uploaded_file(request.FILES['file'])    
                      
    audio = AudioFile() 
    audioFiles =  os.listdir(path)
    return render(request, "home.html", {'form':audio, 'audioFiles':audioFiles})

def run_inference(request):
    model = request.POST.get('model', None)
    audio = request.POST.get('audio', None)

    output = specific_inference(model, audio)
    output = output.decode("utf-8")

    data = {                        
        'output': output,
    }
    return JsonResponse(data)