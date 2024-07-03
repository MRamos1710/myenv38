from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Registro(ComplexModel):
    usuario_id = Unicode
    estado = Unicode

registros = {
    "user1": Registro(usuario_id="user1", estado="pendiente"),
    "user2": Registro(usuario_id="user2", estado="confirmado"),
}

class ServicioConfirmacionRegistro(ServiceBase):
    @rpc(Unicode, _returns=Registro)
    def confirmar_registro(ctx, usuario_id):
        if usuario_id in registros:
            registros[usuario_id].estado = "confirmado"
            return registros[usuario_id]
        return None

application = Application([ServicioConfirmacionRegistro], 'ConfirmacionRegistroApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s51registro?wsdl")
    server.serve_forever()
