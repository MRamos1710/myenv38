from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Ruta(ComplexModel):
    ruta_id = Unicode
    origen = Unicode
    destino = Unicode
    horario = Unicode
    duracion = Unicode

rutas = [
    Ruta(ruta_id="1", origen="Lima", destino="Cusco", horario="08:00", duracion="02:00"),
    Ruta(ruta_id="2", origen="Arequipa", destino="Puno", horario="10:00", duracion="04:00"),
    Ruta(ruta_id="3", origen="Trujillo", destino="Chiclayo", horario="14:00", duracion="01:30")
]

class ServicioRutasEntrega(ServiceBase):
    @rpc(Unicode, _returns=Array(Ruta))
    def listar_rutas(ctx, origen):
        if origen:
            return [ruta for ruta in rutas if origen.lower() in ruta.origen.lower()]
        return rutas

application = Application([ServicioRutasEntrega], 'RutasEntregaApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s24rutas?wsdl")
    server.serve_forever()
