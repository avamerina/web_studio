# Generated by Django 4.2.6 on 2023-10-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]
