from Pago import Pago
from Envio import Envio

# Clase Ventas, con sus atributos respectivos
class Ventas:
    def __init__(self, cliente, productos, cantidades, metodo_pago, metodo_envio, subtotal, descuentos, iva, igtf, total):
        self.cliente = cliente
        self.productos = productos
        self.cantidades = cantidades
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.subtotal = subtotal
        self.descuentos = descuentos
        self.iva = iva
        self.igtf = igtf
        self.total = total
        self.pagos = []  # Se guardan como atributo los pagos realizados
        self.envios = []  # Se guardan como atributo los envios realizados

    def generar_factura(self, clientes): # Funcion que genera una factura a cada cliente registrado en la tienda
        cliente_encontrado = None
        for cliente in clientes:
            if self.cliente == cliente.cedula_rif:
                cliente_encontrado = cliente
                break

        if cliente_encontrado: # Verifica si el cliente es juridico o natural para generar la factura respectiva
            if "J" in cliente_encontrado.cedula_rif[0]:  # Cliente jurídico
                print("Factura a crédito:")
                print(f"Cliente: {cliente_encontrado.nombre}")
                print(f"Productos: {self.productos}")
                print(f"Cantidad: {self.cantidades}")
                print(f"Subtotal: {self.subtotal}")
                print(f"Descuentos: {self.descuentos}")
                print(f"IVA (16%): {self.iva}")
                print(f"Impuesto IGTF (3%): {self.igtf}")
                print(f"Total: {self.total}")
            else:  # Cliente natural
                print("Factura de compra:")
                print(f"Cliente: {cliente_encontrado.nombre}")
                print(f"Productos: {self.productos}")
                print(f"Cantidad: {self.cantidades}")
                print(f"Total: {self.total}")
        else:
            print("Cliente no encontrado. No se puede generar la factura.")

    def registrar_pago(self, cliente, monto, moneda, tipo_pago, fecha): # Funcion que registra un pago en la tienda
        nuevo_pago = Pago(cliente, monto, moneda, tipo_pago, fecha)
        self.pagos.append(nuevo_pago)  # Guardado de un pago con sus atributos
        print("Pago registrado exitosamente.")

    def buscar_pagos(self, cliente=None, fecha=None, tipo_pago=None, moneda=None): # Funcion que filtra una busqueda de un pago
        resultados = []
        for pago in self.pagos: # Dependiendo del filtro seleccionado se busca un pago con dicha caracteristica
            if (cliente is None or pago.cliente == cliente) and                 (fecha is None or pago.fecha == fecha) and                 (tipo_pago is None or pago.tipo_pago == tipo_pago) and                 (moneda is None or pago.moneda == moneda):
                resultados.append(pago)
        return resultados

    def registrar_envio(self, orden_compra, servicio_envio, motorizado=None, costo_servicio=0): # Funcion para registrar un envio 
        nuevo_envio = Envio(orden_compra, servicio_envio, motorizado, costo_servicio)
        self.envios.append(nuevo_envio)
        print("Envío registrado exitosamente.")

    def buscar_envios(self, cliente=None, fecha=None): # Buscar un envio dentro de la tienda
        resultados = []
        for envio in self.envios:
            if (cliente is None or envio.cliente == cliente) and                 (fecha is None or envio.fecha == fecha):
                resultados.append(envio)
        return resultados
