# Generated by Django 2.0.9 on 2018-12-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlApp', '0005_auto_20181230_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='CEO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='fund',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='jojo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='tel_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]