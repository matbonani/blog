# Generated by Django 3.2 on 2022-04-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220402_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
