from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
class Paquete(ComplexModel):
    paquete_id = Unicode
    descripcion = Unicode
    destino = Unicode
    estado = Unicode

paquetes = [
    Paquete(paquete_id="1", descripcion="Electrónicos", destino="Lima", estado="En tránsito"),
    Paquete(paquete_id="2", descripcion="Ropa", destino="Arequipa", estado="En almacén"),
    Paquete(paquete_id="3", descripcion="Libros", destino="Cusco", estado="En almacén"),
    Paquete(paquete_id="4", descripcion="Audifonos", destino="Arequipa", estado="En almacén"),
    Paquete(paquete_id="5", descripcion="Teclados", destino="Cusco", estado="En almacén")
]
class ServicioEnvioPaquete(ServiceBase):
    @rpc(Unicode, _returns=Paquete)
    def enviar_paquete(ctx, paquete_id):
        for paquete in paquetes:
            if paquete.paquete_id == paquete_id:
                paquete.estado = "Enviado"
                return paquete
        return Paquete(paquete_id="0", descripcion="Desconocido", destino="Desconocido", estado="No encontrado")
application = Application([ServicioEnvioPaquete], 'EnvioPaqueteApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)
if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s26paquete?wsdl")
    server.serve_forever()
