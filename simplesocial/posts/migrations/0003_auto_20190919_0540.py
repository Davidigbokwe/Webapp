# Generated by Django 2.2.5 on 2019-09-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190919_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message_html',
            field=models.TextField(default='yes', editable=False),
        ),
    ]