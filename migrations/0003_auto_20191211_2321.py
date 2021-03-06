# Generated by Django 2.1.7 on 2019-12-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0002_auto_20191211_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='demographics_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='leaders_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='lgbt_social_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='mediator_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='proposals_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='qualifier_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='treatment_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
