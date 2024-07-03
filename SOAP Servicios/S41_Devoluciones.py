from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Array, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Devolucion(ComplexModel):
    devolucion_id = Integer
    pedido_id = Integer
    descripcion = Unicode
    monto = Float

devoluciones = [
    Devolucion(devolucion_id=1, pedido_id=101, descripcion="Producto defectuoso", monto=100.0),
    Devolucion(devolucion_id=2, pedido_id=102, descripcion="Error en el pedido", monto=200.0)
]

class ServicioDevoluciones(ServiceBase):
    @rpc(Integer, Unicode, Float, _returns=Unicode)
    def registrar_devolucion(ctx, pedido_id, descripcion, monto):
        nueva_devolucion = Devolucion(devolucion_id=len(devoluciones)+1, pedido_id=pedido_id, descripcion=descripcion, monto=monto)
        devoluciones.append(nueva_devolucion)
        return f"Devolución registrada con ID: {nueva_devolucion.devolucion_id}"

    @rpc(_returns=Array(Devolucion))
    def listar_devoluciones(ctx):
        return devoluciones

application = Application([ServicioDevoluciones], 'ServicioDevoluciones',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s41devoluciones?wsdl")
    server.serve_forever()
