from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Transportista(ComplexModel):
    transportista_id = Integer
    nombre = Unicode
    numero_licencia = Unicode

transportistas = []

class ServicioRegistrarTransportista(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def registrar_transportista(ctx, nombre, numero_licencia):
        nuevo_id = len(transportistas) + 1
        nuevo_transportista = Transportista(transportista_id=nuevo_id, nombre=nombre, numero_licencia=numero_licencia)
        transportistas.append(nuevo_transportista)
        return f"Transportista {nombre} registrado con ID {nuevo_id}"

application = Application([ServicioRegistrarTransportista], 'RegistrarTransportistaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s34transportista?wsdl")
    server.serve_forever()
