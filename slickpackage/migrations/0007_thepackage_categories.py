# Generated by Django 3.0.3 on 2020-03-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slickpackage', '0006_auto_20200313_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='thepackage',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='slickpackage.Categories'),
            preserve_default=False,
        ),
    ]