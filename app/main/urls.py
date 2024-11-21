from django.urls import path
from .views import home, success_page

urlpatterns = [
    path('', home, name='home'),
    path("success_page/", success_page, name="success_page")
]
