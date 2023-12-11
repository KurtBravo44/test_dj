from django.core.mail import send_mail

send_mail(
    'Привет',
    "Как дела?",
    'Gistura@yandex.ru',
    ['Gistura@yandex.ru'],
    fail_silently=False
)

send_mail()