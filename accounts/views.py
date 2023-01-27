from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from accounts.forms import *
#for creating inline formset
from django.forms import inlineformset_factory
#Django filter for search filter
from accounts.filters import OrderFilter

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    
    content = {'title':'Dashboard','orders':orders,'customers':customers,
    'total_customers':total_customers,'total_orders':total_orders,
    'delivered':delivered,'pending':pending}

    return render(request,'accounts/dashboard.html',context=content)

def product(request):
    products = Product.objects.all()
    content = {'title':'Product','products':products}
    return render(request,'accounts/products.html',context=content)

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    content = {'title':'Customer','orders':orders,'customer':customer,'total_orders':total_orders,'myFilter':myFilter}

    print(customer)
    return render(request,'accounts/customer.html',context=content)


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    #formset params = Parent Model, Child Model, Chield model fields
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    # formset = OrderFormSet(instance=customer)
    #for hiding existing order
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'form':formset,'title':'Create Order'}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'title':'Update Order'}
    return render(request,'accounts/order_form.html',context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'title':'Create Customer'}
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'title':'Delete Order','order':order,'item':order}
    return render(request,'accounts/delete.html',context)
