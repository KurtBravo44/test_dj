# Generated by Django 5.0 on 2023-12-10 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='имя')),
                ('middle_name', models.CharField(max_length=25, verbose_name='отчество')),
                ('last_name', models.CharField(max_length=25, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=100, verbose_name='почта')),
                ('message', models.TextField(blank=True, null=True, verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='SettingsMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='начало')),
                ('stop', models.DateTimeField(verbose_name='конец')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Еженедельная'), ('monthly', 'Ежемесячная')], default='daily', max_length=25, verbose_name='период')),
                ('status', models.CharField(max_length=25, verbose_name='статус')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
