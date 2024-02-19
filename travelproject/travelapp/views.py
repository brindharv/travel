from django.shortcuts import render
from . models import travel
from . models import team

# Create your views here.
def demo(request):
    obj = travel.objects.all()
    obje = team.objects.all()
    return render(request,"index.html",{'result':obj,'res':obje})

