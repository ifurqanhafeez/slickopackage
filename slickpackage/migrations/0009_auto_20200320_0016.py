# Generated by Django 3.0.3 on 2020-03-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slickpackage', '0008_auto_20200317_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('image01', models.ImageField(blank=True, null=True, upload_to='')),
                ('image02', models.ImageField(blank=True, null=True, upload_to='')),
                ('image03', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='industryproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('image01', models.ImageField(blank=True, null=True, upload_to='')),
                ('image02', models.ImageField(blank=True, null=True, upload_to='')),
                ('image03', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='industry',
        ),
    ]
