from spyne import Application, rpc, ServiceBase, Unicode, Float, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class PagoReserva(ComplexModel):
    usuario_id = Unicode
    monto = Float
    estado = Unicode

pagos_reserva = {}

class ServicioPagoReserva(ServiceBase):
    @rpc(Unicode, Float, _returns=PagoReserva)
    def registrar_pago(ctx, usuario_id, monto):
        if usuario_id not in pagos_reserva:
            pagos_reserva[usuario_id] = PagoReserva(usuario_id=usuario_id, monto=monto, estado="pendiente")
        else:
            pagos_reserva[usuario_id].monto += monto
        pagos_reserva[usuario_id].estado = "completado"
        return pagos_reserva[usuario_id]

application = Application([ServicioPagoReserva], 'PagoReservaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s52pago?wsdl")
    server.serve_forever()
