from django.contrib import admin

from mailing.models import Client, SettingsMail, MessageMail, LogsMail


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'middle_name',
                    'email',
                    'message',)
    list_filter = ('first_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(SettingsMail)
class SettingsMailAdmin(admin.ModelAdmin):
    list_display = ('owner', 'start', 'stop', 'period', 'status',)
    list_filter = ('status',)
    search_fields = ('owner',)


@admin.register(MessageMail)
class MessageMailAdmin(admin.ModelAdmin):
    list_display = ('mail_key', 'title', 'body',)
    list_filter = ('mail_key',)
    search_fields = ('title',)


@admin.register(LogsMail)
class LogsMailAdmin(admin.ModelAdmin):
    list_display = ('mail_key', 'status_try', 'date_try', 'response',)
    list_filter = ('status_try',)


