from spyne import Application, rpc, ServiceBase, Unicode, Array, ComplexModel, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Proveedor(ComplexModel):
    ruc = Unicode
    direccion = Unicode
    razon_social = Unicode
    disponible = Boolean

proveedores = [
    Proveedor(ruc="123456789", direccion="Dirección 1", razon_social="Razón Social 1", disponible=True),
    Proveedor(ruc="987654321", direccion="Dirección 2", razon_social="Razón Social 2", disponible=True),
    Proveedor(ruc="456789123", direccion="Dirección 3", razon_social="Razón Social 3", disponible=True)
]

class ProveedorService(ServiceBase):
    @rpc(Unicode, _returns=Array(Proveedor))
    def listar_proveedores(ctx, nombre):
        if nombre:
            return [p for p in proveedores if nombre in p.razon_social]
        return proveedores

application = Application([ProveedorService], 'ProveedorApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    server.serve_forever()
