from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from .utils import send_telegram_notification
from .serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet

def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            message_text = f"Новый заказ от {order.name}!\nТема: {order.topic}\nОписание: {order.description}\nНомер: {order.phone_number}\nТип: {order.document_type}\nСрок: {order.deadline}!"

            send_mail(f'Заказ на {order.document_type}', message_text,
                settings.DEFAULT_FROM_EMAIL,  # От кого
                ['zt20061113@gmail.com', 'adulovbilal001@gmail.com', 'nazilova001@gmail.com', 'tunukaijanyshova@gmail.com'],
                fail_silently=False,
            )
            
            send_telegram_notification(message_text)

            messages.success(request, 'Заказ успешно создан!')

            return redirect('success_page')  # Укажите свой путь для успешной отправки
        else:
            messages.error(request, f'Пожалуйста, исправьте ошибки в форме и заполните пустые поля: {form.errors}')

    else:
        form = OrderForm()

    return render(request, 'main/home.html', {'form': form})

def success_page(request):
    return render(request, 'main/success_page.html')  # Укажите свой путь для страницы успешной отправки



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer