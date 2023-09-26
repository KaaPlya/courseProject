# Generated by Django 4.2.5 on 2023-09-26 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
