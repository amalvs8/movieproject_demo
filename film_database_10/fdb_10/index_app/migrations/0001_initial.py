# Generated by Django 4.2.3 on 2023-07-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250)),
                ('f_year', models.CharField(max_length=250)),
                ('f_genre', models.CharField(max_length=250)),
                ('f_prate', models.CharField(max_length=250)),
                ('f_cast', models.CharField(max_length=250)),
                ('f_dir', models.CharField(max_length=250)),
                ('f_plot', models.TextField()),
                ('f_img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]