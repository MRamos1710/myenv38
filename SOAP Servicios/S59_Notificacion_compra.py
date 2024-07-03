from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Notificacion(ComplexModel):
    usuario_id = Unicode
    compra_id = Integer
    estado = Unicode

notificaciones = {}

class ServicioNotificacion(ServiceBase):
    @rpc(Unicode, Integer, _returns=Notificacion)
    def notificar_compra(ctx, usuario_id, compra_id):
        key = (usuario_id, compra_id)
        if key not in notificaciones:
            notificaciones[key] = Notificacion(usuario_id=usuario_id, compra_id=compra_id, estado="notificado")
        else:
            notificaciones[key].estado = "actualizado"
        return notificaciones[key]

application = Application([ServicioNotificacion], 'NotificacionApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s59notificacion?wsdl")
    server.serve_forever()
