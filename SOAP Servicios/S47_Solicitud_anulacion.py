from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class SolicitudAnulacion(ComplexModel):
    solicitud_id = Integer
    estado = Unicode

solicitudes = []

class ServicioSolicitudAnulacion(ServiceBase):
    @rpc(Integer, _returns=SolicitudAnulacion)
    def anular_solicitud(ctx, solicitud_id):
        for solicitud in solicitudes:
            if solicitud.solicitud_id == solicitud_id:
                solicitud.estado = "anulada"
                return solicitud
        nueva_solicitud = SolicitudAnulacion(solicitud_id=solicitud_id, estado="anulada")
        solicitudes.append(nueva_solicitud)
        return nueva_solicitud

application = Application([ServicioSolicitudAnulacion], 'SolicitudAnulacionApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s47anulacion?wsdl")
    server.serve_forever()
