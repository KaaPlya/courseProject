# Generated by Django 4.2.5 on 2023-09-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='mobile_no',
            field=models.CharField(max_length=15),
        ),
    ]