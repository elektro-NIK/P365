# Generated by Django 2.1.3 on 2018-12-23 18:26

from django.db import migrations, models
import profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_profilemodel_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='pic',
            field=models.ImageField(default='media/avatars/default/default.png', upload_to=profile.models.avatar_user_path),
        ),
    ]