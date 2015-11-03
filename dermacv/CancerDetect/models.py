from django.db import models
import os
# Create your models here.

def update_filename(instance, filename):
    path = "uploads/"
    idx=str(IMGUpload.objects.all().aggregate(models.Max('id'))['id__max'])
    if idx=='None':
	idx='0'
    return path+idx+'.jpg'

class IMGUpload(models.Model):
	
	posted_on = models.DateTimeField(auto_now_add=True, editable=False)
	uploaded_img = models.ImageField(upload_to=update_filename)
	
	
	def __unicode__(self):
		return os.path.basename(self.uploaded_img.name)
