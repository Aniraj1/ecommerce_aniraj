from django.urls import path
from .views import index, cart, removecart #search, 


urlpatterns = [
    path('', index),
    # path('search/', search),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
]