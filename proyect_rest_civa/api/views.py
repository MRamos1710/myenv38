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
    url = 'http://localhost:8081/recepcionEncomienda'
    data = {
        "registro_encomienda_id": 3,
        "peso": 10.5,
        "clasificacion": "Electrónicos",
        "tipo_producto": "Teléfono",
        "detalles": "iPhone 13 Pro",
        "ubicacion_actual": "Arequipa"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)
    

def s5_destinatario(request):
    if request.method == 'POST':
        url = 'http://localhost:8081/destinatario'
        data = {
            "nombre": "Ana Gomez",
            "correo": "ana.gomez@example.com",
            "contrasena": "hashedpassword123"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({"error": "Failed to send request"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


def s6_registro_encomienda(request):
    if request.method == 'POST':
        url = 'http://localhost:8081/registroEncomienda'
        data = {
            "remitente_id": 1,
            "destinatario_id": 2,
            "fecha_recogida": "2024-07-01",
            "direccion_recogida": "Calle Falsa 123, Lima"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({"error": "Failed to send request"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)