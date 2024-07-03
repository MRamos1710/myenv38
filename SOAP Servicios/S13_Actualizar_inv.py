from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Inventario(ComplexModel):
    articulo_id = Integer
    nombre_articulo = Unicode
    cantidad = Integer
    precio = Float

inventario = [
    Inventario(articulo_id=1, nombre_articulo="Monitor", cantidad=50, precio=199.99),
    Inventario(articulo_id=2, nombre_articulo="Teclado", cantidad=150, precio=29.99),
    Inventario(articulo_id=3, nombre_articulo="Mouse", cantidad=200, precio=19.99),
]

class ServicioActualizarInventario(ServiceBase):
    @rpc(Integer, Integer, _returns=Unicode)
    def actualizar_inventario(ctx, articulo_id, nueva_cantidad):
        for articulo in inventario:
            if articulo.articulo_id == articulo_id:
                articulo.cantidad = nueva_cantidad
                return f"Artículo {articulo.nombre_articulo} actualizado con nueva cantidad {nueva_cantidad}"
        return "Artículo no encontrado"

application = Application([ServicioActualizarInventario], 'ActualizarInventarioApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s13inventario?wsdl")
    server.serve_forever()
