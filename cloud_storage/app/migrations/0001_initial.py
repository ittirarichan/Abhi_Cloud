# Generated by Django 5.1.3 on 2024-12-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
                ('audio', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
    ]