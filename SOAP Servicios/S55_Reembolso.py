from spyne import Application, rpc, ServiceBase, Unicode, Float, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Reembolso(ComplexModel):
    usuario_id = Unicode
    monto = Float
    estado = Unicode

reembolsos = {}

class ServicioReembolso(ServiceBase):
    @rpc(Unicode, Float, _returns=Reembolso)
    def procesar_reembolso(ctx, usuario_id, monto):
        if usuario_id not in reembolsos:
            reembolsos[usuario_id] = Reembolso(usuario_id=usuario_id, monto=monto, estado="pendiente")
        else:
            reembolsos[usuario_id].monto += monto
        reembolsos[usuario_id].estado = "completado"
        return reembolsos[usuario_id]

application = Application([ServicioReembolso], 'ReembolsoApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s55reembolso?wsdl")
    server.serve_forever()
