from spyne import Application, rpc, ServiceBase, Unicode, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Reporte(ComplexModel):
    reporte_id = Unicode
    tipo = Unicode
    descripcion = Unicode
    estado = Unicode

reportes = [
    Reporte(reporte_id="1", tipo="daño", descripcion="Pantalla rota", estado="Pendiente"),
    Reporte(reporte_id="2", tipo="pérdida", descripcion="Paquete perdido en tránsito", estado="Resuelto"),
    Reporte(reporte_id="3", tipo="daño", descripcion="Caja dañada", estado="Pendiente")
]

class ServicioGestionDaniosPerdidas(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Reporte)
    def gestionar_reporte(ctx, reporte_id, accion):
        for reporte in reportes:
            if reporte.reporte_id == reporte_id:
                if accion == "marcar_como_resuelto":
                    reporte.estado = "Resuelto"
                elif accion == "marcar_como_pendiente":
                    reporte.estado = "Pendiente"
                return reporte
        return Reporte(reporte_id="0", tipo="Desconocido", descripcion="No encontrado", estado="No encontrado")

application = Application([ServicioGestionDaniosPerdidas], 'GestionDaniosPerdidasApp',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on port 8000...")
    print("WSDL available at: http://localhost:8000/s31gestion?wsdl")
    server.serve_forever()
