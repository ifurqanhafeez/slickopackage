# Generated by Django 3.0.3 on 2020-03-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slickpackage', '0010_industryproduct_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sunject', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
    ]
