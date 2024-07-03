from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, DateTime
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from datetime import datetime

class PaqueteFaltante(ComplexModel):
    paquete_id = Integer
    descripcion = Unicode
    fecha_registro = DateTime

paquetes_faltantes = []

class ServicioRegistroPaquetesFaltantes(ServiceBase):
    @rpc(Integer, Unicode, DateTime, _returns=Unicode)
    def registrar_paquete_faltante(ctx, paquete_id, descripcion, fecha_registro):
        nuevo_paquete = PaqueteFaltante(paquete_id=paquete_id, descripcion=descripcion, fecha_registro=fecha_registro)
        paquetes_faltantes.append(nuevo_paquete)
        return f"Paquete faltante con ID {paquete_id} registrado correctamente"

application = Application([ServicioRegistroPaquetesFaltantes], 'RegistroPaquetesFaltantesApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s37paquetesfaltantes?wsdl")
    server.serve_forever()
