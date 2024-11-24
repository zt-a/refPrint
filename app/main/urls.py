from django.urls import path, include
from .views import home, success_page
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', home, name='home'),
    path("success_page/", success_page, name="success_page"),
    path('api/', include(router.urls)),
]
