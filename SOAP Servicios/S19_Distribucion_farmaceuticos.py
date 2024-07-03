from spyne import Application, rpc, ServiceBase, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Farmaceutico(ComplexModel):
    farmaceutico_id = Unicode
    nombre = Unicode
    descripcion = Unicode
    ubicacion_actual = Unicode

farmaceuticos = [
    Farmaceutico(farmaceutico_id="1", nombre="Aspirina", descripcion="Analgésico", ubicacion_actual="Almacén Central, Lima"),
    Farmaceutico(farmaceutico_id="2", nombre="Paracetamol", descripcion="Antipirético", ubicacion_actual="Sucursal Arequipa"),
    Farmaceutico(farmaceutico_id="3", nombre="Ibuprofeno", descripcion="Antiinflamatorio", ubicacion_actual="Sucursal Trujillo")
]

class ServicioDistribucionFarmaceuticos(ServiceBase):
    @rpc(_returns=Array(Farmaceutico))
    def listar_farmaceuticos(ctx):
        return farmaceuticos

application = Application([ServicioDistribucionFarmaceuticos], 'DistribucionFarmaceuticosApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s19farmaceuticos?wsdl")
    server.serve_forever()
