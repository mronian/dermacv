# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import CancerDetect.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMGUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('uploaded_img', models.ImageField(upload_to=CancerDetect.models.update_filename)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
