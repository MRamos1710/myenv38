from spyne import Application, rpc, ServiceBase, Unicode, Array, ComplexModel, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Encomienda(ComplexModel):
    registro_encomienda_id = Unicode
    peso = Float
    clasificacion = Unicode
    tipo_producto = Unicode
    detalles = Unicode
    ubicacion_actual = Unicode

encomiendas_express = [
    Encomienda(registro_encomienda_id="1", peso=2.5, clasificacion="Documentos", tipo_producto="Papel", 
               detalles="Contrato Urgente", ubicacion_actual="Sucursal Central, Lima"),
    Encomienda(registro_encomienda_id="2", peso=1.0, clasificacion="Electrónicos", tipo_producto="Pendrive", 
               detalles="Pendrive 64GB", ubicacion_actual="Centro de distribución, Arequipa")
]

class ServicioEntregaExpress(ServiceBase):
    @rpc(_returns=Array(Encomienda))
    def listar_encomiendas_express(ctx):
        return encomiendas_express

application = Application([ServicioEntregaExpress], 'ServicioEntregaExpress',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s16entregaexpress?wsdl")
    server.serve_forever()
