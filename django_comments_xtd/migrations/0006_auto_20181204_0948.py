# Generated by Django 2.1.3 on 2018-12-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0005_auto_20170920_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtdcomment',
            name='followup',
            field=models.BooleanField(blank=True, default=False, help_text='Notify follow-up comments'),
        ),
    ]
