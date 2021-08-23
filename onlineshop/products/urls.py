from django.urls import path

from .views import ProductsView, OneProductView

app_name = 'products'


urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<id>', OneProductView.as_view())
]
