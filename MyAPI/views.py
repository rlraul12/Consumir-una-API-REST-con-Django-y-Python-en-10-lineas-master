from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
# Importando Libreria Requests para hacer solicitudes HTTP
import requests


def getAPI(request):
    # URL de productos
    URL_API = "https://jsonplaceholder.typicode.com/albums"

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API)

    if response.status_code == 200:
        # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
        productos = response.json()
        """
        for producto in productos:
            print(producto)
        """
        return HttpResponse(productos) or []


def obtener_productos(request):
    URL_API = "https://fakestoreapi.com/products"
    try:
        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API)
        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
            productos = response.json()
        else:
            # En caso de un código de respuesta no exitoso, manejar de acuerdo a tus necesidades
            print(f"Error en la solicitud: {response.status_code}")
            productos = []
    except requests.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        print(f"Error en la solicitud: {e}")
        productos = []

    return render(request, 'index.html', {'productos': productos})


def product_detail(request, product_id):
    URL_API = 'https://fakestoreapi.com/products/'
  
    # Construir la URL completa con el ID del producto
    product_url = f'{URL_API}{product_id}'
    
    # Hacer la solicitud GET a la API
    response = requests.get(product_url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta en formato JSON
        product_data = response.json()
        return render(request, 'product_detail.html', {'producto': product_data})
    else:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
@require_http_methods(["GET", "POST"])
def delete_product(request, product_id):
    URL_API = 'https://fakestoreapi.com/products/'
    product_url = f'{URL_API}{product_id}'

    if request.method == 'POST':
        response = requests.delete(product_url)
        if response.status_code == 200:
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Failed to delete product'}, status=response.status_code)

    # Si el método es GET, simplemente renderiza la confirmación de eliminación
    return render(request, 'confirm_delete.html', {'product_id': product_id})