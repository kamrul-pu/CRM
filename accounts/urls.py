from django.urls import path
# from .views import home,product,customer,createOrder,updateOrder,createCustomer,deleteOrder,loginPage,registerPage,userLogout,userPage,accountSettings
from accounts.views import *
from django.contrib.auth import views as auth_view

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
    
    # path('reset_password/',auth_view.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password/',auth_view.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name='reset_password'),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uid64>/<token>',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('mail/',mail,name='mail')
]

"""

from django.contrib.auth import views as auth_view
1 - Submit email form //PasswordResetView.as_view())
2 - Email Sent Success Message //PasswordResetDoneView.as_view()),
3 - Link to password Reset form in email //PasswordResetConfirmView.as_view()),
4 - Password Successfully changed message //PasswordResetCompleteView.as_view()),
"""