# Generated by Django 4.1.3 on 2022-11-22 02:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='email',
        ),
        migrations.AddField(
            model_name='familia',
            name='FechaNac',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
