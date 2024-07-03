from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, DateTime
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from datetime import datetime

class AlmacenamientoLargoPlazo(ComplexModel):
    item_id = Integer
    nombre = Unicode
    descripcion = Unicode
    fecha_almacenamiento = DateTime

almacenamientos = []

class ServicioAlmacenamientoLargoPlazo(ServiceBase):
    @rpc(Integer, Unicode, Unicode, DateTime, _returns=Unicode)
    def almacenar_item(ctx, item_id, nombre, descripcion, fecha_almacenamiento):
        nuevo_item = AlmacenamientoLargoPlazo(item_id=item_id, nombre=nombre, descripcion=descripcion, fecha_almacenamiento=fecha_almacenamiento)
        almacenamientos.append(nuevo_item)
        return f"Item con ID {item_id} almacenado correctamente"

application = Application([ServicioAlmacenamientoLargoPlazo], 'AlmacenamientoLargoPlazoApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s39almacenamientolargo?wsdl")
    server.serve_forever()
