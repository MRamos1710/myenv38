from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Incidente(ComplexModel):
    incidente_id = Integer
    descripcion = Unicode
    estado = Unicode

incidentes = [
    Incidente(incidente_id=1, descripcion="Retraso en la entrega", estado="Pendiente"),
    Incidente(incidente_id=2, descripcion="Producto dañado", estado="Resuelto"),
    Incidente(incidente_id=3, descripcion="Paquete extraviado", estado="Pendiente")
]

class ServicioInformeIncidentes(ServiceBase):
    @rpc(Integer, Unicode, _returns=Incidente)
    def actualizar_informe(ctx, incidente_id, estado):
        for incidente in incidentes:
            if incidente.incidente_id == incidente_id:
                incidente.estado = estado
                return incidente
        return Incidente(incidente_id=0, descripcion="No encontrado", estado="No encontrado")

application = Application([ServicioInformeIncidentes], 'InformeIncidentesApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s32informe?wsdl")
    server.serve_forever()
