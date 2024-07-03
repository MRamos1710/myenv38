from spyne import Application, rpc, ServiceBase, ComplexModel, Array, Integer, Decimal, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Encomienda(ComplexModel):
    registro_encomienda_id = Integer
    peso = Decimal
    clasificacion = Unicode
    tipo_producto = Unicode
    detalles = Unicode
    ubicacion_actual = Unicode

encomiendas = [
    Encomienda(registro_encomienda_id=1, peso=10.5, clasificacion="Electrónicos", tipo_producto="Teléfono", detalles="iPhone 13 Pro", ubicacion_actual="Centro de distribución, Lima"),
    Encomienda(registro_encomienda_id=2, peso=5.0, clasificacion="Documentos", tipo_producto="Papel", detalles="Contrato", ubicacion_actual="Sucursal Central, Lima")
]

class EncomiendaService(ServiceBase):
    @rpc(_returns=Array(Encomienda))
    def listar_encomiendas(ctx):
        return encomiendas

application = Application([EncomiendaService], 'EncomiendaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL is available at: http://localhost:8000/s4encomienda?wsdl")
    server.serve_forever()
