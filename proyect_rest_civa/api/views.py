import requests
from django.http import JsonResponse

def s1_cotizacion(request):
    url = 'http://localhost:8081/cotizacion'
    data = {
        "usuario_id": 1,
        "monto": 150.00,
        "estado": "pendiente"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)

def s2_emisor(request):
    url = 'http://localhost:8081/emisor'
    data = {
        "nombre": "Desde Python",
        "correo": "pruebapython@example.com",
        "contrasena": "123123"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)
    
def s3_encomienda(request):
    url = 'http://localhost:8081/encomienda'
    data = {
        "registro_encomienda_id": 1,
        "peso": 10.5,
        "clasificacion": "Prueba Py",
        "tipo_producto": "Teléfono",
        "detalles": "iPhone 15 Pro"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)