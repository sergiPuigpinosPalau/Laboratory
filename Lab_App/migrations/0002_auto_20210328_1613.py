# Generated by Django 3.1.7 on 2021-03-28 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Administrator_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scientist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Scientist_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]