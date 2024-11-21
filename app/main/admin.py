from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    # Список полей, которые отображаются в административной панели
    list_display = ('id', 'is_completed', 'document_type', 'topic', 'deadline', 'created_at', 'name', 'phone_number')  # Укажите нужные поля
    
    # Фильтры для административной панели
    list_filter = ('is_completed', 'document_type', 'created_at')  # Добавьте фильтрацию по типу документа и дате создания
    
    # Поиск по полям в административной панели
    search_fields = ('name', 'phone_number', 'topic', 'is_completed', 'document_type', 'deadline')  # Укажите поля, по которым можно будет искать

# Регистрация модели и ее настроек в админке
admin.site.register(Order, OrderAdmin)