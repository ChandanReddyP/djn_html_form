from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

def html_forms(request):

    if request.method=='POST':
        return HttpResponse('post method is activated')

    return render(request,'html_forms.html')



def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        To=Topic.objects.get_or_create(topic_name=topic)[0]
        To.save()
        return HttpResponse('Topic is created')
    
    return render(request,'insert_topic.html')


