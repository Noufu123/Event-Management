# Generated by Django 3.2.9 on 2022-07-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_photo', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('product_name', models.CharField(max_length=250)),
                ('product_parice', models.IntegerField()),
            ],
        ),
    ]
