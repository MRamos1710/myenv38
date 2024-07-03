from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Alimento(ComplexModel):
    alimento_id = Unicode
    nombre = Unicode
    descripcion = Unicode
    ubicacion_actual = Unicode

alimentos = [
    Alimento(alimento_id="1", nombre="Manzanas", descripcion="Frutas frescas", ubicacion_actual="Almacén Central, Lima"),
    Alimento(alimento_id="2", nombre="Arroz", descripcion="Grano básico", ubicacion_actual="Sucursal Arequipa"),
    Alimento(alimento_id="3", nombre="Carne", descripcion="Carne fresca", ubicacion_actual="Sucursal Trujillo")
]
class ServicioDistribucionAlimentos(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def distribuir_alimento(ctx, alimento_id):
        for alimento in alimentos:
            if alimento.alimento_id == alimento_id:
                return f"Distribuyendo {alimento.nombre} con descripción: {alimento.descripcion} desde {alimento.ubicacion_actual}"
        return "Alimento no encontrado"

application = Application([ServicioDistribucionAlimentos], 'DistribucionAlimentosApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)
if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s20alimentos?wsdl")
    server.serve_forever()
