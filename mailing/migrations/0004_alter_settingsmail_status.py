# Generated by Django 5.0 on 2023-12-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_logsmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmail',
            name='status',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='статус'),
        ),
    ]