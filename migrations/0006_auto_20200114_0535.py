# Generated by Django 2.1.7 on 2020-01-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0005_auto_20200114_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='country_from_1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_from_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_from_3',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_from_4',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_from_5',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_to_1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_to_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_to_3',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_to_4',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='participant',
            name='country_to_5',
            field=models.TextField(default=''),
        ),
    ]
