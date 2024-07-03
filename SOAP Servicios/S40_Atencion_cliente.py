from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ConsultaCliente(ComplexModel):
    consulta_id = Integer
    cliente_id = Integer
    descripcion = Unicode

consultas_cliente = [
    ConsultaCliente(consulta_id=1, cliente_id=100, descripcion="Consulta sobre el estado del pedido."),
    ConsultaCliente(consulta_id=2, cliente_id=101, descripcion="Problema con la entrega del producto."),
    ConsultaCliente(consulta_id=3, cliente_id=102, descripcion="Solicitud de devolución de un artículo.")
]

class ServicioAtencionCliente(ServiceBase):
    @rpc(Integer, Unicode, _returns=Unicode)
    def registrar_consulta(ctx, cliente_id, descripcion):
        nueva_consulta = ConsultaCliente(consulta_id=len(consultas_cliente) + 1, cliente_id=cliente_id, descripcion=descripcion)
        consultas_cliente.append(nueva_consulta)
        return f"Consulta registrada correctamente con ID {nueva_consulta.consulta_id}"

    @rpc(Integer, _returns=ConsultaCliente)
    def obtener_consulta(ctx, consulta_id):
        for consulta in consultas_cliente:
            if consulta.consulta_id == consulta_id:
                return consulta
        return None

application = Application([ServicioAtencionCliente], 'AtencionClienteApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s40atencioncliente?wsdl")
    server.serve_forever()
