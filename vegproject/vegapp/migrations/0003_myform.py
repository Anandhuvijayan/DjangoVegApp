# Generated by Django 3.0.1 on 2020-01-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegapp', '0002_responseform'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
