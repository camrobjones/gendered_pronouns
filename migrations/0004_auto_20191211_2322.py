# Generated by Django 2.1.7 on 2019-12-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0003_auto_20191211_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='lgbt_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
