# Generated by Django 4.1.7 on 2023-05-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0009_missing'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing',
            name='missing_image',
            field=models.ImageField(default=1, upload_to='static/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='missing',
            name='missing_phone',
            field=models.CharField(max_length=100),
        ),
    ]
