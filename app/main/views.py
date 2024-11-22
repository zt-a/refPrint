from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from .utils import send_telegram_notification

def home(request):
    if request.method == 'POST':
        # Если вы используете Django Form, используйте её для валидации данных
        form = OrderForm(request.POST)

        if form.is_valid():
            # Если форма валидна, сохраняем данные в базе данных
            order = form.save()

            send_mail(
                'Новый заказ!',
                f'Заказ от {order.name}:\nТема: {order.topic}\nОписание: {order.description}',
                settings.DEFAULT_FROM_EMAIL,  # От кого
                ['zt20061113@gmail.com', 'adulovbilal001@gmail.com', 'nazilova001@gmail.com', 'tunukaijanyshova@gmail.com'],
                fail_silently=False,
            )
            
            telegram_message = f"Новый заказ от {order.name}!\nТема: {order.topic}\nОписание: {order.description}"
            send_telegram_notification(telegram_message)

            # Выводим сообщение об успешной отправке
            messages.success(request, 'Заказ успешно создан!')

            # Перенаправляем на страницу успеха
            return redirect('success_page')  # Укажите свой путь для успешной отправки
        else:
            # Если форма не валидна, возвращаем пользователю ошибки
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме и заполните пустые поля.')

    else:
        # Если метод GET, создаем пустую форму
        form = OrderForm()

    return render(request, 'main/home.html', {'form': form})

def success_page(request):
    return render(request, 'main/success_page.html')  # Укажите свой путь для страницы успешной отправки