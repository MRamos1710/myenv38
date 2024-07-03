
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import *

urlpatterns = [
    path('s1_cotizacion/', s1_cotizacion, name='s1_cotizacion'),
    path('s2_emisor/', s2_emisor, name='s2_emisor'),
    path('s3_encomienda/', s3_encomienda, name='s3_encomienda'),
    path('s5_destinatario/', s5_destinatario, name='s5_destinatario'),
    path('s6_registro_encomienda/', s6_registro_encomienda, name='s6_registro_encomienda'),
    path('s7_modalidad_pago/', s7_modalidad_pago, name='s7_modalidad_pago'),
    path('s8_control_pago/', s8_control_pago, name='s8_control_pago'),
    path('s10_generar_comprobante/', s10_generar_comprobante, name='s10_generar_comprobante'),
    path('s11_registrar_pago/', s11_registrar_pago, name='s11_registrar_pago'),
    path('s12_cambio_destino/', s12_cambio_destino, name='s12_cambio_destino'),
    path('s14_seleccion_encomienda/', s14_seleccion_encomienda, name='s14_seleccion_encomienda'),
    path('s15_etiqueta_clasificacion/', s15_etiqueta_clasificacion, name='s15_etiqueta_clasificacion'),
    path('s21_consulta_conductores/', s21_consulta_conductores, name='s21_consulta_conductores'),
    path('s22_consulta_unidades/', s22_consulta_unidades, name='s22_consulta_unidades'),
    path('s23_fecha_llegada/<int:encomienda_id>/', s23_fecha_llegada, name='s23_fecha_llegada'),
    path('s27_registro_envios/', s27_registro_envios, name='s27_registro_envios'),
    path('s28_rastreo_seguimiento/<int:encomienda_id>/', s28_rastreo_seguimiento, name='s28_rastreo_seguimiento'),
    path('s29_localizacion_agencias/', s29_localizacion_agencias, name='s29_localizacion_agencias'),
    path('s30_envios_a_destinatario/', s30_envios_a_destinatario, name='s30_envios_a_destinatario'),
    path('s35_inventario_repuestos/', s35_inventario_repuestos, name='s35_inventario_repuestos'),
    path('s45_ingresar_datos_usuario/', s45_ingresar_datos_usuario, name='s45_ingresar_datos_usuario'),
    path('s46_datos_reserva/', s46_datos_reserva, name='s46_datos_reserva'),   
    path('s49_proceso_pago/', s49_proceso_pago, name='s49_proceso_pago'),
    path('s50_verificacion_identidad/', s50_verificacion_identidad, name='s50_verificacion_identidad'),
    path('s56_consulta_rutas_horarios/', s56_consulta_rutas_horarios, name='s56_consulta_rutas_horarios'),
    path('s57_emision_boletos/', s57_emision_boletos, name='s57_emision_boletos'),
    path('s58_emision_boletos_electronicos/', s58_emision_boletos_electronicos, name='s58_emision_boletos_electronicos'),

]