# Generated by Django 4.1.7 on 2023-05-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0003_insert_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='insert_staff',
            name='insert_staff_midd_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
