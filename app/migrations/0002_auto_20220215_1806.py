# Generated by Django 3.2.8 on 2022-02-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boshagurung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('gurring', models.TextField(default='', max_length=225, null=True, verbose_name='Izoh')),
            ],
        ),
        migrations.AlterField(
            model_name='foods',
            name='file',
            field=models.FileField(default=0, null=True, upload_to=''),
        ),
    ]
