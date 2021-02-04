from django.shortcuts import render
from django.http import FileResponse
from .forms import ConvertLink
from .converter import convert

# Create your views here.

def index(request):
    if request.method == "POST":
        return FileResponse(open(convert(request.POST["name"]),'rb'), as_attachment=True)
    
    form = ConvertLink()
    
    return render(request, "index.html", {"form":form})

