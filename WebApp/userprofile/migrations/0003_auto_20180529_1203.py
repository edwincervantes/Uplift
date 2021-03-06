# Generated by Django 2.0.3 on 2018-05-29 16:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0002_auto_20180529_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstDayClean', models.DateTimeField(default=datetime.datetime(2018, 5, 29, 12, 3, 11, 341275))),
                ('securityQuestion1', models.CharField(max_length=500)),
                ('securityQuestion2', models.CharField(max_length=500)),
                ('securityAnswer1', models.CharField(max_length=500)),
                ('securityAnswer2', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
