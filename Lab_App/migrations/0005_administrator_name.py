# Generated by Django 3.1.7 on 2021-03-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_App', '0004_auto_20210329_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
