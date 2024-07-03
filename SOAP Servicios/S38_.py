from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, DateTime
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from datetime import datetime

class PlanificacionEntrega(ComplexModel):
    entrega_id = Integer
    descripcion = Unicode
    fecha_planificacion = DateTime

planificaciones_entrega = []

class ServicioPlanificacionEntrega(ServiceBase):
    @rpc(Integer, Unicode, DateTime, _returns=Unicode)
    def planificar_entrega(ctx, entrega_id, descripcion, fecha_planificacion):
        nueva_entrega = PlanificacionEntrega(entrega_id=entrega_id, descripcion=descripcion, fecha_planificacion=fecha_planificacion)
        planificaciones_entrega.append(nueva_entrega)
        return f"Entrega con ID {entrega_id} planificada correctamente"

application = Application([ServicioPlanificacionEntrega], 'PlanificacionEntregaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s38planificacionentrega?wsdl")
    server.serve_forever()
