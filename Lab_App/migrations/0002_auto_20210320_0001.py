# Generated by Django 3.1.7 on 2021-03-19 23:01

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('body', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('version', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_numb', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='experiments',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
