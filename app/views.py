from django.shortcuts import render
from app.models import *
from django.db.models.functions  import Length

# Create your views here.
def model(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().filter(topic_name='basketball')
    d={'topics':QLTO}
    return render(request,'model.html',d)



def webpage(request):
    WLTO=Webpage.objects.all()
    WLTO=Webpage.objects.all().order_by('-name')
    WLTO=Webpage.objects.all().exclude(name='virat')

    d={'web':WLTO}
    return render(request,'webpage.html',d)


def access(request):
    ALTO=AccessRecord.objects.all()
    ALTO=AccessRecord.objects.all().order_by(Length('author').desc())
    
  
    d={'access':ALTO}
    return render (request,'access.html',d)
 


def insert_topic(request):
    tn=input('enter topic name')
    NTo=Topic.objects.get_or_create(topic_name=tn)[0]
    NTo.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render (request,'model.html',d)



  






