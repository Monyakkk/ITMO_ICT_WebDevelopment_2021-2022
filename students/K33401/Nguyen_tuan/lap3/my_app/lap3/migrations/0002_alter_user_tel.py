# Generated by Django 3.2.9 on 2021-12-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lap3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telephone'),
        ),
    ]
