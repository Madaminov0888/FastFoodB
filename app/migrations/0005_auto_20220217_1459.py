# Generated by Django 3.2.8 on 2022-02-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220217_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='chat_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
