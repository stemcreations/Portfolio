# Generated by Django 4.2.5 on 2023-09-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_image_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]