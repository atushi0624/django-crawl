# Generated by Django 2.0.9 on 2018-12-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_time', models.DateTimeField()),
                ('is_technology', models.BooleanField(default=False)),
                ('is_mobile', models.BooleanField(default=False)),
                ('is_app', models.BooleanField(default=False)),
                ('is_entertainment', models.BooleanField(default=False)),
                ('is_beauty', models.BooleanField(default=False)),
                ('is_fashion', models.BooleanField(default=False)),
                ('is_lifestyle', models.BooleanField(default=False)),
                ('is_business', models.BooleanField(default=False)),
                ('is_gourmet', models.BooleanField(default=False)),
                ('is_sports', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('PRtimes_URL', models.URLField()),
                ('official_URL', models.URLField()),
                ('category', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('tel_number', models.IntegerField()),
                ('CEO', models.CharField(max_length=20)),
                ('jojo', models.CharField(max_length=20)),
                ('fund', models.CharField(max_length=20)),
                ('is_client', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawlApp.CompanyInfo'),
        ),
    ]