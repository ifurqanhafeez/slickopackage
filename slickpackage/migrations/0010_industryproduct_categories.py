# Generated by Django 3.0.3 on 2020-03-19 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slickpackage', '0009_auto_20200320_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='industryproduct',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='slickpackage.IndCategories'),
            preserve_default=False,
        ),
    ]