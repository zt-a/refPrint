from django.db import models

class Order(models.Model):
    # Возможные варианты для типа документа
    DOCUMENT_TYPE_CHOICES = [
        ('referat', 'Реферат'),
        ('referat_handwritten', 'Реферат (от руки)'),
        ('consplect_lecture', 'Конспект, Лекция'),
        ('presentation', 'Презентация'),
    ]

    # Поле для имени
    name = models.CharField(max_length=255, verbose_name="Имя")

    # Поле для номера телефона
    phone_number = models.CharField(max_length=15, verbose_name="Тел. Номер")

    # Поле для типа документа с выбором из фиксированного списка
    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES,
        default='referat',  # Можно указать значение по умолчанию
        verbose_name="Тип документа"
    )

    # Поле для названия темы
    topic = models.CharField(max_length=255, verbose_name="Тема")

    # Поле для описания
    description = models.TextField(verbose_name="Описание")

    # Поле для статуса "Выполнен"
    is_completed = models.BooleanField(default=False, verbose_name="Выполнен")
    deadline = models.DateField(null=True, blank=True, verbose_name="Срок")

    # Временные метки
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновление")

    def __str__(self):
        return f"{self.id} - {self.name}: {self.topic} ! {self.deadline}"
