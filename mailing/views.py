from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from mailing.models import Client, SettingsMail, MessageMail


class MailingCreateView(CreateView):
    model = Client
    fields = ('first_name', 'middle_name', 'last_name', 'email', 'message',)
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.save()

        return super().form_valid(form)


class ClientListView(ListView):
    model = Client


class MailingSettingsCreateView(CreateView):
    model = SettingsMail
    template_name = 'mailing/mailingsettings_form.html'
    fields = ('owner', 'start', 'stop', 'period',)

    success_url = reverse_lazy('mailing:mailings')

class MailingListView(ListView):
    model = SettingsMail
    template_name = 'mailing/mailing_list.html'


class MailingSettingsUpdateView(UpdateView):
    model = SettingsMail
    template_name = 'mailing/mailingsettings_form.html'
    fields = ('owner', 'start', 'stop', 'period',)

    success_url = reverse_lazy('mailing:mailings')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()

        return super().form_valid(form)


class MessageMailCreateView(CreateView):
    model = MessageMail

    template_name = 'mailing/messagemail_form.html'
    fields = ('mail_key', 'title', 'body',)
    success_url = reverse_lazy('mailing:mailings')

    def form_valid(self, form):
        if form.is_valid():
            new_message = form.save()
            new_message.save()

        return super().form_valid(form)

class MessageMailListView(ListView):
    model = MessageMail
    template_name = 'mailing/messagemail_list.html'


class MessageMailUpdateView(UpdateView):
    model = MessageMail
    template_name = 'mailing/messagemail_form.html'
    fields = ('mail_key', 'title', 'body',)

    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()

        return super().form_valid(form)


