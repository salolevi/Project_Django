# Generated by Django 3.2.9 on 2021-11-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analist',
            name='password',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]