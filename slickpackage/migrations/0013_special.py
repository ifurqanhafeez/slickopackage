# Generated by Django 3.0.3 on 2020-03-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slickpackage', '0012_auto_20200320_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
