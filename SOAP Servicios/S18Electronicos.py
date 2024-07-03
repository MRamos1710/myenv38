from spyne import Application, rpc, ServiceBase, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Electronico(ComplexModel):
    electronico_id = Unicode
    marca = Unicode
    modelo = Unicode
    especificaciones = Unicode
    ubicacion_actual = Unicode

electronicos = [
    Electronico(electronico_id="1", marca="Apple", modelo="iPhone 13 Pro", especificaciones="128GB, 5G", ubicacion_actual="Oficina Central, Lima"),
    Electronico(electronico_id="2", marca="Dell", modelo="XPS 15", especificaciones="16GB RAM, 512GB SSD", ubicacion_actual="Sucursal Arequipa"),
    Electronico(electronico_id="3", marca="Apple", modelo="iPad Pro", especificaciones="256GB, WiFi", ubicacion_actual="Oficina Trujillo")
]

class ServicioDistribucionElectronicos(ServiceBase):
    @rpc(_returns=Array(Electronico))
    def listar_electronicos(ctx):
        return electronicos

application = Application([ServicioDistribucionElectronicos], 'DistribucionElectronicosApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s18electronicos?wsdl")
    server.serve_forever()
