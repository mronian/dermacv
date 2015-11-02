from django.shortcuts import render

# Create your views here.
import os
import sys
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
#from OCR.models import DocUpload, UserProfile
#from OCR.forms import DocUploadForm, UserForm, UserProfileForm
#from tasks import start
CV_CODE_PATH=settings.BASE_DIR+'/CVCode/'
sys.path.insert(0, CV_CODE_PATH)
    
def upload(request):
    if request.method == 'POST':
        form = DocUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocUpload(uploaded_doc = request.FILES['uploaded_doc'])
            newdoc.save()
            IMAGE_PATH=str(newdoc)
            start.delay(IMAGE_PATH)
            return HttpResponseRedirect('/CancerDetect/result')
        else:
            print form.errors
            return HttpResponse('image upload failed')
    else:
        form=DocUploadForm()
    
    context_dict = {'boldmessage': "CancerDetect", 'form':form}
    return render(request, 'CancerDetect/index.html', context_dict)

def result(request):
    return