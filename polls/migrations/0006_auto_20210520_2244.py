# Generated by Django 3.1.1 on 2021-05-20 17:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]