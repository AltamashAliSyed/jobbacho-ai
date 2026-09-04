from django.shortcuts import render
from .ollama import analyze_job
# Create your views here.
def detector(request):
    message = None
    result = None
    if request.method =="POST":
        message=request.POST.get("job_message")
        result = analyze_job(message)
    return render(request,'home.html',{"message":message,"result":result})