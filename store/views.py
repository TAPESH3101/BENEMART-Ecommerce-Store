from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .utils import *
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order=data['order']
    items=data['items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}

    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    print(context)

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    else:
        customer, order = guestOrder(request,data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    return JsonResponse("Payment complete..", safe=False)

def jeans(request):
    return render(request, 'store/jeans.html')

def slipper(request):
    return render(request, 'store/slipper.html')

def rog(request):
    return render(request, 'store/Rog.html')

def samsung(request):
    return render(request, 'store/Samsung.html')

def vivo(request):
    return render(request, 'store/Vivo.html')

def watch(request):
    return render(request, 'store/WATCH.html')

def asus(request):
    return render(request, 'store/ASUSVivobook.html')

def macbook(request):
    return render(request, 'store/MacBook.html')

def buds(request):
    return render(request, 'store/earbuds.html')

def iphone(request):
    return render(request, 'store/iphone.html')

def tv(request):
    return render(request, 'store/tv.html')

def backpack(request):
    return render(request, 'store/backpack.html')

def pendrive(request):
    return render(request, 'store/pendrive.html')

def writingpad(request):
    return render(request, 'store/writingpad.html')

def dumbell(request):
    return render(request, 'store/dumbell.html')