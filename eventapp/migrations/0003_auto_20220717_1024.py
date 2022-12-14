# Generated by Django 3.2.9 on 2022-07-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ser_Photo', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('Ser_Name', models.CharField(max_length=25)),
                ('Ser_Price', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='product_parice',
            new_name='product_price',
        ),
    ]
