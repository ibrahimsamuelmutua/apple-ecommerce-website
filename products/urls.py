from django.urls import path
from . import views as sam

urlpatterns = [
    path('', sam.products, name='products-url'),
    path('add-products/', sam.add_products, name='add-products-url'),
    path('delete-product/<id>', sam.delete, name='delete-url'),
    path('update-products/<id>', sam.update_products, name='update-url'),
    path('pay/<id>', sam.pay, name='payment-url'),

]
