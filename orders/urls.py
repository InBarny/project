from django.urls import path
from . import views
# йоу

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
