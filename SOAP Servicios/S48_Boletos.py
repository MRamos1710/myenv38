from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Boleto(ComplexModel):
    boleto_id = Integer
    numero_boleto = Unicode
    estado = Unicode

boletos = [
    Boleto(boleto_id=1, numero_boleto="BOL123", estado="disponible"),
    Boleto(boleto_id=2, numero_boleto="BOL456", estado="vendido"),
    Boleto(boleto_id=3, numero_boleto="BOL789", estado="disponible")
]

class ServicioSeleccionBoletos(ServiceBase):
    @rpc(Integer, _returns=Boleto)
    def seleccionar_boleto(ctx, boleto_id):
        for boleto in boletos:
            if boleto.boleto_id == boleto_id:
                boleto.estado = "vendido"
                return boleto
        return None

application = Application([ServicioSeleccionBoletos], 'SeleccionBoletosApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s48boletos?wsdl")
    server.serve_forever()
