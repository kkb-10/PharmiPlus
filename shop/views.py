from django.http import HttpResponse
from .models import Product, Contact,Orders,OrderUpdate
from django.contrib import messages
from math import ceil
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

def start(request):
    return render(request, 'shop/start.html')

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allProds =[]
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))        
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    if request.user.is_anonymous:
        return render(request, 'shop/login.html')
    return render(request, 'shop/index.html',params)

def about(request):
    if request.user.is_authenticated:
        return render(request, 'shop/about.html')
    return render(request, 'shop/login.html')
    

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        messages.success(request, 'Your message has been sent!')
    return render(request, 'shop/contact.html', {'thank': thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        user = ''
        if request.user.is_authenticated:
            user = request.user.username
        try:
            order = Orders.objects.filter(order_id=orderId, user=user)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
    
        

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    
    return render(request, 'shop/prodView.html', {'product':product[0]})        





def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        user = ''
        if request.user.is_authenticated:
            user = request.user.username
        # email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, user=user, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/shop/home/")

        else:
            # No backend authenticated the credentials
            return render(request, 'shop/login.html')

    return render(request, 'shop/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/shop")

def register(request):

#form= UserCreationForm()
    if request.method =="POST":
       form= UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("/shop/login")
    else:
        form= UserCreationForm()
    return render(request,'shop/register.html' ,{'form':form})