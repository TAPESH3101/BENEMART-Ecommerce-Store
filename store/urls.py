from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('jeans', views.jeans, name='jeans'),
	path('slipper', views.slipper, name='slipper'),
	path('asus', views.asus, name='asus'),
	path('macbook', views.macbook, name='macbook'),
	path('samsung', views.samsung, name='samsung'),
	path('vivo', views.vivo, name='vivo'),
	path('watch', views.watch, name='watch'),
	path('rog', views.rog, name='rog'),
	path('buds', views.buds, name='buds'),
	path('iphone', views.iphone, name='iphone'),
	path('tv', views.tv, name='tv'),
	path('backpack', views.backpack, name='backpack'),
	path('pendrive', views.pendrive, name='pendrive'),
	path('writingpad', views.writingpad, name='writingpad'),
	path('dumbell', views.dumbell, name='dumbell'),
]



[['*', '.', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '.', '*', '.'] ,
[ '*', '.', '*', '#', '*', '.', '*', '#', '.', '*', '.', '#', '*', '*', '*', '*', '*', '*' ],
[ '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '*', '.', '*' ] ]