# Generated by Django 3.2 on 2021-04-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
