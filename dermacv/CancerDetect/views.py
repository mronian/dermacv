from django.shortcuts import render

# Create your views here.
import os
import sys
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
#from OCR.models import DocUpload, UserProfile
#from OCR.forms import DocUploadForm, UserForm, UserProfileForm
from tasks import start
CV_CODE_PATH=settings.BASE_DIR+'/CVCode/'
sys.path.insert(0, CV_CODE_PATH)
import FieldExtract
from FieldExtract import getFields
import weka.core.jvm as jvm

def index(request):
    #print os.listdir(settings.BASE_DIR)
    #print settings.BASE_DIR
    
    jvm.start()
    ADMIN_T=False
    USER_T=False
    if request.user.is_authenticated()==True :
        profile=UserProfile.objects.get(user=request.user)
        if profile.account_type=='Admin':
            ADMIN_T=True
        elif profile.account_type=='User':
            USER_T=True

    context_dict = {'boldmessage': "ResearchUSA", 'Admin' : ADMIN_T, 'User' : USER_T}
    return render(request, 'OCR/index.html', context_dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        profile=UserProfile.objects.get(user=user)
        
        if user:
            if user.is_active:
                login(request, user)
                if profile.account_type=='Admin':
                    return HttpResponseRedirect('/OCR/admin/')
                elif profile.account_type=='User':
                    return HttpResponseRedirect('/OCR/user/')
            else:
                return HttpResponse("Your ResearchUSA account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'OCR/login.html', {})
    