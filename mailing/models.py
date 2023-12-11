from django.db import models

NULLABLE = {'null':True, 'blank':True}

periods =(
    ('daily', 'Ежедневная'),
    ('weekly', 'Еженедельная'),
    ('monthly', 'Ежемесячная'),
)

class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='имя')
    middle_name = models.CharField(max_length=25, verbose_name='отчество')
    last_name = models.CharField(max_length=25, verbose_name='фамилия')
    email = models.EmailField(max_length=100, verbose_name='почта')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'Клиент: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class SettingsMail(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    start = models.DateTimeField(verbose_name='начало')
    stop = models.DateTimeField(verbose_name='конец')
    period = models.CharField(max_length=25, choices=periods, default='daily', verbose_name='период')
    status = models.CharField(max_length=25, verbose_name='статус', **NULLABLE)

    def __str__(self):
        return f'Рассылка: {self.owner}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class MessageMail(models.Model):
    mail_key = models.ForeignKey(SettingsMail, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'Содержимое: {self.mail_key}'

    class Meta:
        verbose_name = 'Содержимое'
        verbose_name_plural = 'Содержимое'


class LogsMail(models.Model):
    mail_key = models.ForeignKey(SettingsMail, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    date_try = models.DateTimeField(verbose_name='последняя попытка', **NULLABLE)
    status_try = models.CharField(max_length=25, verbose_name='статус попытки', **NULLABLE)
    response = models.TextField(verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return f'Логи рассылки: {self.mail_key}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
