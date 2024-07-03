from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Campana(ComplexModel):
    campana_id = Integer
    nombre = Unicode
    descripcion = Unicode

campanas = [
    Campana(campana_id=1, nombre="Campaña Verano", descripcion="Promoción de viajes a la costa"),
    Campana(campana_id=2, nombre="Campaña Invierno", descripcion="Descuentos en viajes a Cusco")
]

class ServicioMarketing(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def registrar_campana(ctx, campana_id, nombre, descripcion):
        nueva_campana = Campana(campana_id=campana_id, nombre=nombre, descripcion=descripcion)
        campanas.append(nueva_campana)
        return f"Campaña registrada con ID: {nueva_campana.campana_id}"

    @rpc(_returns=Array(Campana))
    def listar_campanas(ctx):
        return campanas

application = Application([ServicioMarketing], 'ServicioMarketingApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s43marketing?wsdl")
    server.serve_forever()
