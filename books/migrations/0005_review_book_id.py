# Generated by Django 3.2 on 2021-04-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=1),
        ),
    ]
