from rest_framework import serializers
from .models import Order
from .utils import send_telegram_notification
from django.core.mail import send_mail
from django.conf import settings



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'document_type', 'topic', 'description', 'deadline']
        
    def create(self, validated_data):
        order = super().create(validated_data)
        
        message_text = f"Новый заказ от {order.name}!\nТема: {order.topic}\nОписание: {order.description}\nНомер: {order.phone_number}\nТип: {order.document_type}\nСрок: {order.deadline}!"
        
        send_telegram_notification(message_text)

        send_mail(f'Заказ на {order.document_type}', message_text,
                settings.DEFAULT_FROM_EMAIL,  # От кого
                ['zt20061113@gmail.com', 'adulovbilal001@gmail.com', 'nazilova001@gmail.com', 'tunukaijanyshova@gmail.com'],
                fail_silently=False,
            )

        return order
