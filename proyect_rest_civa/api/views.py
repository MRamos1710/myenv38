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
    url = 'http://localhost:8081/destinatario'
    data = {
            "nombre": "Prueba Python",
            "correo": "mramos1@ingenium.edu.pee", #Cambiar correo esta como key
            "contrasena": "asdsadasdd"
        }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)



def s6_registro_encomienda(request):
    url = 'http://localhost:8081/registroEncomienda'
    data = {
        "remitente_id": 1,
        "destinatario_id": 2,
        "fecha_recogida": "2024-07-01",
        "direccion_recogida": "Calle Falsa 123, Lima",
        "fecha_estimada_llegada": "2024-09-20"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)
    


def s7_modalidad_pago(request):
    url = 'http://localhost:8081/modalidadPago'
    data = {
        "usuario_id": 1,
        "modo_pago": "tarjeta_credito",
        "monto": 100.50
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send request"}, status=500)

def s8_control_pago(request):
    url = 'http://localhost:8081/controlPago?usuario_id=1'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)
    
def s10_generar_comprobante(request):

        url = 'http://localhost:8081/generarComprobante'
        data = {
            "usuario_id": 1,
            "pago_id": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({"error": "Failed to generate receipt"}, status=500)
        
def s11_registrar_pago(request):
    url = 'http://localhost:8081/registrarPago'
    data = {
        "usuario_id": 1, #Variar ide para cambiar estado
        "monto": 150.75,
        "modo_pago": "tarjeta_credito"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to register payment"}, status=500)
    
def s12_cambio_destino(request):
    url = 'http://localhost:8081/cambioDestino'
    data = {
        "encomienda_id": 1,
        "nuevo_destino": "Nueva dirección desde Py"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to change destination"}, status=500)
    
def s14_seleccion_encomienda(request):
    url = 'http://localhost:8081/seleccionEncomienda'
    data = {
        "encomienda_id": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to select shipment"}, status=500)
    
def s15_etiqueta_clasificacion(request):
    url = 'http://localhost:8081/etiquetaClasificacion'
    data = {
        "encomienda_id": 1,
        "etiqueta": "Nueva Etiqueta",
        "clasificacion": "Nueva Clasificación"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to update label and classification"}, status=500)
    
def s21_consulta_conductores(request):
    url = 'http://localhost:8081/conductores'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch drivers data"}, status=500)
    
def s22_consulta_unidades(request):
    url = 'http://localhost:8081/unidades'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch units data"}, status=500)
    
def s22_consulta_unidades(request):
    url = 'http://localhost:8081/unidades'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch units data"}, status=500)
    
def s23_fecha_llegada(request, encomienda_id):
    url = f'http://localhost:8081/fechaLlegada/{encomienda_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to determine arrival date"}, status=500)
    
def s27_registro_envios(request):
    url = 'http://localhost:8081/registroEnvios'
    data = {
        "remitente_id": 1,
        "destinatario_id": 2,
        "fecha_recogida": "2024-07-01",
        "direccion_recogida": "CAlle Prueba desde Aplicacion",
        "fecha_estimada_llegada": "2024-07-05"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to register shipment"}, status=500)
    
def s28_rastreo_seguimiento(request, encomienda_id):
    url = f'http://localhost:8081/rastreo/{encomienda_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch tracking data"}, status=500)
    
def s29_localizacion_agencias(request):
    url = 'http://localhost:8081/agencias'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch agencies data"}, status=500)
    
def s30_envios_a_destinatario(request):
    url = 'http://localhost:8081/enviosADestinatario'
    data = {
        "encomienda_id": 1,
        "estado": "Enviado al destinatario"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to send shipment to recipient"}, status=500)
    
def s35_inventario_repuestos(request):
    url = 'http://localhost:8081/inventario'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch inventory data"}, status=500)
    
def s45_ingresar_datos_usuario(request):
    url = 'http://localhost:8081/ingresarDatosUsuario'
    data = {
        "nombre": "Juan Perez",
        "correo": "pruebapyppz@example.com",
        "contrasena": "password123",
        "tipo_usuario": "emisor"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to enter user data"}, status=500)
    
def s46_datos_reserva(request):
    reserva_id = request.GET.get('reserva_id')
    if not reserva_id:
        return JsonResponse({"error": "Missing reserva_id parameter"}, status=400)
    
    url = f'http://localhost:8081/datosReserva?reserva_id={reserva_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch reservation data"}, status=500)
    
def s49_proceso_pago(request): #falta probar
    url = 'http://localhost:8081/procesoDePago'
    data = {
        "usuario_id": 1,
        "monto": 100,
        "modo_pago": "tarjeta"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to process payment"}, status=500)
    

def s50_verificacion_identidad(request): #falta probar
    url = 'http://localhost:8081/verificarIdentidad'
    data = {
        "usuario_id": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to verify identity"}, status=500)
    

def s54_verificacion_elegibilidad(request):
    url = 'http://localhost:8081/verificarElegibilidad'
    data = {
        "usuario_id": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to verify eligibility"}, status=500)
    
def s56_consulta_rutas_horarios(request):
    url = 'http://localhost:8081/rutasHorarios'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch routes and schedules data"}, status=500)
    
def s57_emision_boletos(request):
    url = 'http://localhost:8081/emitirBoleto'
    data = {
        "usuario_id": 1,
        "ruta_id": 11,
        "numero_boleto": "BOL123",
        "estado_boleto": "activo"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to issue ticket"}, status=500)
    
def s58_emision_boletos_electronicos(request):
    url = 'http://localhost:8081/emitirBoletoElectronico'
    data = {
        "usuario_id": 2,
        "ruta_id": 12,
        "numero_boleto": "BELEC456",
        "estado_boleto": "activo"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to issue electronic ticket"}, status=500)