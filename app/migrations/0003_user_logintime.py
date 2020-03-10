# Generated by Django 3.0 on 2020-03-09 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_logintime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='loginTime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
