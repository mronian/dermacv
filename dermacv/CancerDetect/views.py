from django.shortcuts import render

# Create your views here.
import os
import sys
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from CancerDetect.models import IMGUpload
from CancerDetect.forms import IMGUploadForm
#from tasks import start
CV_CODE_PATH=settings.BASE_DIR+'/CVCode/'
sys.path.insert(0, CV_CODE_PATH)

from tasks import start
    
def upload(request):
    if request.method == 'POST':
        form = IMGUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = IMGUpload(uploaded_img = request.FILES['uploaded_img'])
            newimg.save()
            IMAGE_PATH=str(newimg)
            print IMAGE_PATH
            start.delay(IMAGE_PATH)
            print "DONE"
            #return HttpResponseRedirect('/CancerDetect/')
        else:
            print form.errors
            return HttpResponse('image upload failed')
    else:
        form=IMGUploadForm()
    
    context_dict = {'boldmessage': "CancerDetect", 'form': form}
    return render(request, 'CancerDetect/index.html', context_dict)

def result(request):
    return