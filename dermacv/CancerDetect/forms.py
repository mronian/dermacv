from django import forms
from CancerDetect.models import IMGUpload

class IMGUploadForm(forms.ModelForm):
    uploaded_img=forms.ImageField()
    class Meta:
        model = IMGUpload
        fields = ('uploaded_img',)
        