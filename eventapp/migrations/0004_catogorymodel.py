# Generated by Django 3.2.9 on 2022-07-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_auto_20220717_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='catogoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catgory_Name', models.CharField(max_length=250)),
            ],
        ),
    ]
