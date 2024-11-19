# Clase Envio, con sus atributos respectivos
class Envio:
    def __init__(self, orden_compra, servicio_envio, motorizado=None, costo_servicio=0):
        self.orden_compra = orden_compra
        self.servicio_envio = servicio_envio
        self.motorizado = motorizado
        self.costo_servicio = costo_servicio
