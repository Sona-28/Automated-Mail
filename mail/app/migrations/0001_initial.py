# Generated by Django 4.1.1 on 2022-10-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Att',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
                ('subject', models.CharField(max_length=100)),
                ('attach', models.FileField(upload_to='')),
                ('message', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('inquiry', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Upld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('inquiry', models.CharField(max_length=70, null=True)),
                ('message', models.CharField(max_length=170, null=True)),
            ],
        ),
    ]
