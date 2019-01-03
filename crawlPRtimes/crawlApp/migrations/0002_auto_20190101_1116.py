# Generated by Django 2.0.9 on 2019-01-01 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawlApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='app',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='beauty',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='business',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='entertainment',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='fashion',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='gourmet',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='lifestyle',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='sports',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='technology',
        ),
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='タグ名'),
            preserve_default=False,
        ),
    ]