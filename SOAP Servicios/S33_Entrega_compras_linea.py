from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Compra(ComplexModel):
    compra_id = Integer
    producto = Unicode
    cantidad = Integer
    precio = Decimal
    estado = Unicode

compras = [
    Compra(compra_id=1, producto="Laptop", cantidad=1, precio=1200.00, estado="Pendiente"),
    Compra(compra_id=2, producto="Smartphone", cantidad=2, precio=800.00, estado="Enviado"),
    Compra(compra_id=3, producto="Tablet", cantidad=3, precio=300.00, estado="Entregado")
]

class ServicioEntregaCompras(ServiceBase):
    @rpc(Integer, _returns=Compra)
    def consultar_compra(ctx, compra_id):
        for compra in compras:
            if compra.compra_id == compra_id:
                return compra
        return Compra(compra_id=0, producto="No encontrado", cantidad=0, precio=0.00, estado="No encontrado")

application = Application([ServicioEntregaCompras], 'EntregaComprasApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s33entrega?wsdl")
    server.serve_forever()
