# Generated by Django 2.0.9 on 2018-12-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlApp', '0004_auto_20181223_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='tel_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]