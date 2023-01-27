from django.forms import ModelForm
from accounts.models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ('customer','product','status')
        fields = "__all__"

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"