from django.urls import path, include
from product.views import index, categories, product_detail

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:id>', categories, name='category'),
    path('detail/<int:id>', product_detail, name='detail'),
]