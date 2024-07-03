from spyne import Application, rpc, ServiceBase, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Documento(ComplexModel):
    documento_id = Unicode
    tipo = Unicode
    descripcion = Unicode
    ubicacion_actual = Unicode

documentos = [
    Documento(documento_id="1", tipo="Contrato", descripcion="Contrato de alquiler", ubicacion_actual="Oficina Central, Lima"),
    Documento(documento_id="2", tipo="Reporte", descripcion="Reporte anual de ventas", ubicacion_actual="Sucursal Arequipa"),
    Documento(documento_id="3", tipo="Factura", descripcion="Factura de compra", ubicacion_actual="Oficina Trujillo")
]

class ServicioDistribucionDocumentos(ServiceBase):
    @rpc(_returns=Array(Documento))
    def listar_documentos(ctx):
        return documentos

application = Application([ServicioDistribucionDocumentos], 'DistribucionDocumentosApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s17documentos?wsdl")
    server.serve_forever()
