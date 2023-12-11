from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    ClientListView, MessageMailCreateView, MessageMailListView, MessageMailUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingCreateView.as_view(), name='home'),
    path('list/', ClientListView.as_view(), name='list'),
    path('settings/', MailingSettingsCreateView.as_view(), name='settings'),
    path('edit/<int:pk>', MailingSettingsUpdateView.as_view(), name='edit'),
    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('message/', MessageMailCreateView.as_view(), name='message'),
    path('message_list', MessageMailListView.as_view(), name='message_list'),
    path('message_edit/<int:pk>', MessageMailUpdateView.as_view(), name='message_edit'),

]