# Generated by Django 3.0.1 on 2019-12-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_heading', models.CharField(max_length=100)),
                ('blog_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('blog_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
