# Generated by Django 2.1.5 on 2020-07-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]