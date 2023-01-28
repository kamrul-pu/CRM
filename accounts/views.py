from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from accounts.models import *
from accounts.forms import *
#for creating inline formset
from django.forms import inlineformset_factory
#Django filter for search filters custom
from accounts.filters import OrderFilter
from accounts.decorators import *

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username:',username,'password:',password)
        user = authenticate(username=username,password=password)
        if user is not None:
            print("Valid User")
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'accounts/login.html',context={})
        # form = AuthenticationForm()

        # context = {'title':"Login Page",'form':form}
    return render(request,'accounts/login.html',context={})

@login_required
def userLogout(request):
    logout(request)
    return redirect('home')
@unauthenticated_user
def registerPage(request):
    # form = UserCreationForm()
    form = CreateUserForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # user.save()
            messages.success(request,f"Hello {username}, Account Created Successfully")
            return redirect('login')
    context = {'form':form,'title':'User Creatation Form'}
    return render(request,'accounts/register.html',context)

@login_required
@admin_only
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

@login_required
@allowed_users(allowed_roles='customer')
def userPage(request):
    orders = request.user.customer.order_set.all()
    print("customer",request.user.customer.profile_pic)

    total_orders = orders.count()
    delivered = Order.objects.filter(status='Delivered',customer=request.user.customer).count()
    pending = Order.objects.filter(status='Pending',customer=request.user.customer).count()
    context = {'title':'User Profile','orders':orders,'total_orders':total_orders,
    'delivered':delivered,'pending':pending}
    return render(request,'accounts/user.html',context)

@login_required
@allowed_users(allowed_roles='customer')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            print("Profile saved")
        else:
            print("Not Saved")
            # if 'profile_pic' in request.FILES:
            #     form.profile_pic = request.FILES['profile_pic']
            # form.save()
    context = {'title':'Account Update','form':form}
    return render(request,'accounts/accounts_settings.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()
    content = {'title':'Product','products':products}
    return render(request,'accounts/products.html',context=content)

@login_required
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    content = {'title':'Customer','orders':orders,'customer':customer,'total_orders':total_orders,'myFilter':myFilter}

    print(customer)
    return render(request,'accounts/customer.html',context=content)

@login_required
@allowed_users(allowed_roles=['admin'])
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

@login_required
@allowed_users(allowed_roles=['admin'])
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

@login_required
@allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'title':'Create Customer'}
    return render(request,'accounts/order_form.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'title':'Delete Order','order':order,'item':order}
    return render(request,'accounts/delete.html',context)



from django.http import HttpResponse  
# from djangoapp import settings
from django.conf import settings
from django.core.mail import send_mail  
  
"""email send functions"""

def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "mkamrulh219@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  
