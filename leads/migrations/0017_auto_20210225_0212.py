# Generated by Django 3.1.5 on 2021-02-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_auto_20210224_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.jpg', upload_to='uploads/profile_pictures'),
        ),
    ]
