from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Cuenta(ComplexModel):
    cuenta_id = Integer
    nombre = Unicode
    correo = Unicode
    estado = Unicode

cuentas = []

class ServicioCreacionCuenta(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Cuenta)
    def crear_cuenta(ctx, nombre, correo):
        cuenta_id = len(cuentas) + 1
        nueva_cuenta = Cuenta(cuenta_id=cuenta_id, nombre=nombre, correo=correo, estado="activa")
        cuentas.append(nueva_cuenta)
        return nueva_cuenta

application = Application([ServicioCreacionCuenta], 'ServicioCreacionCuentaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s44creacioncuenta?wsdl")
    server.serve_forever()
