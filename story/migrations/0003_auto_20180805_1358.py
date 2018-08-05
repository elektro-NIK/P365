# Generated by Django 2.0.7 on 2018-08-05 13:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_storymodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storymodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
