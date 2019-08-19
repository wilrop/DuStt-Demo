from django.shortcuts import render
from django.http import HttpResponse
from .functions import handle_uploaded_file, run_inference 
from .forms import AudioFile 


def index(request):
    if request.method == 'POST':  
        audio = AudioFile(request.POST, request.FILES)  
        if audio.is_valid():  
            handle_uploaded_file(request.FILES['file'])
            output = run_inference(request.FILES['file'], "/Users/willemropke/Documents/BT-projects/Models/30-1024-00055-2-NOC.pb")  
            return HttpResponse("Inferred output: " +  output.decode("utf-8"))
    else:  
        audio = AudioFile()  
    return render(request, "home.html", {'form':audio})
