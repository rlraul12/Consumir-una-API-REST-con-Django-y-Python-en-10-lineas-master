from django.urls import path
# Importando desde views.py la funcion obtener_productos()
from . import views
from .views import getAPI, obtener_productos

urlpatterns = [
    path('', obtener_productos, name='obtener_productos'),
    path('producto/<int:product_id>',views.product_detail, name='product_detail'),
    path('product/<int:product_id>/', views.delete_product, name='delete_product'),

    path('api/', getAPI, name='getAPI'),
]
