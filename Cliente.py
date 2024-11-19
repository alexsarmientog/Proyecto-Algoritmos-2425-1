# Clase Cliente, con sus atributos respectivos
class Cliente:
    def __init__(self, nombre, apellido, cedula_rif, correo, direccion, telefono, es_juridico=False, nombre_contacto=None, telefono_contacto=None, correo_contacto=None):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula_rif = cedula_rif
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.es_juridico = es_juridico
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
