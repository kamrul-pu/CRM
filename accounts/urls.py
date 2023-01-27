from django.urls import path
from .views import home,product,customer,createOrder,updateOrder,createCustomer,deleteOrder
urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('customer/<int:pk>/',customer,name='customer'),
    path('create_order/<int:pk>/',createOrder,name='create_order'),
    path('update_order/<int:pk>/',updateOrder,name='update_order'),
    path('create_customer/',createCustomer,name='create_customer'),
    path('delete_order/<int:pk>/',deleteOrder,name='delete_order'),
]