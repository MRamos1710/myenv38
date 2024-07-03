from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class QuejaReclamacion(ComplexModel):
    queja_id = Integer
    descripcion = Unicode
    estado = Unicode

quejas_reclamaciones = [
    QuejaReclamacion(queja_id=1, descripcion="Producto dañado", estado="Pendiente"),
    QuejaReclamacion(queja_id=2, descripcion="Entrega tardía", estado="Resuelto")
]

class ServicioQuejasReclamaciones(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def registrar_queja(ctx, queja_id, descripcion, estado):
        nueva_queja = QuejaReclamacion(queja_id=queja_id, descripcion=descripcion, estado=estado)
        quejas_reclamaciones.append(nueva_queja)
        return f"Queja/Reclamación registrada con ID: {nueva_queja.queja_id}"

    @rpc(_returns=Array(QuejaReclamacion))
    def listar_quejas(ctx):
        return quejas_reclamaciones

application = Application([ServicioQuejasReclamaciones], 'ServicioQuejasReclamaciones',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s42quejas?wsdl")
    server.serve_forever()
