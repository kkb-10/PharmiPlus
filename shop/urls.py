
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker', views.tracker,name="TrackingStatus"),
    path('search/', views.search,name="Search"),
    path('products/<int:myid>', views.productView,name="ProductView"),
    path('checkout/', views.checkout,name="Checkout"),
]
