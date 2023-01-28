from django.urls import path
from .views import home,product,customer,createOrder,updateOrder,createCustomer,deleteOrder,loginPage,registerPage,userLogout,userPage,accountSettings


urlpatterns = [
    path('login/',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',userLogout,name='logout'),
    path('user/',userPage,name='user_page'),
    path('account/',accountSettings,name='account'),
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('customer/<int:pk>/',customer,name='customer'),
    path('create_order/<int:pk>/',createOrder,name='create_order'),
    path('update_order/<int:pk>/',updateOrder,name='update_order'),
    path('create_customer/',createCustomer,name='create_customer'),
    path('delete_order/<int:pk>/',deleteOrder,name='delete_order'),
]