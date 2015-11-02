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

def index(request):
    #print os.listdir(settings.BASE_DIR)
    #print settings.BASE_DIR

    return render(request, 'CancerDetect/index.html', {})
    