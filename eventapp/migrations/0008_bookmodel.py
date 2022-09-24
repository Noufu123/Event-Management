# Generated by Django 3.2.9 on 2022-07-21 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventapp', '0007_servicemodel_ser'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdct', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventapp.productmodel')),
                ('ser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventapp.servicemodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
