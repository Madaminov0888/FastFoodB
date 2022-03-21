from django.contrib import admin
from .models import Boshagurung, BotUser, Foods



@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'full_name', 'savat']


@admin.register(Foods)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['type', 'title', 'sum']

@admin.register(Boshagurung)
class GurrungAdmin(admin.ModelAdmin):
    list_display = ['title', 'gurring']