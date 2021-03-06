# Generated by Django 3.1.5 on 2021-02-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_auto_20210225_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
