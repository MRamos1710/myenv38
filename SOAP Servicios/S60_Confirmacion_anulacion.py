from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Anulacion(ComplexModel):
    usuario_id = Unicode
    boleto_id = Integer
    estado = Unicode

anulaciones = {}

class ServicioAnulacion(ServiceBase):
    @rpc(Unicode, Integer, _returns=Anulacion)
    def confirmar_anulacion(ctx, usuario_id, boleto_id):
        key = (usuario_id, boleto_id)
        if key not in anulaciones:
            anulaciones[key] = Anulacion(usuario_id=usuario_id, boleto_id=boleto_id, estado="confirmado")
        else:
            anulaciones[key].estado = "actualizado"
        return anulaciones[key]

application = Application([ServicioAnulacion], 'AnulacionApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s60anulacion?wsdl")
    server.serve_forever()
