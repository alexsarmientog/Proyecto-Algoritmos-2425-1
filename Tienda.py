import requests # Inclusion de librerias
import json
import sys
import os
from collections import Counter
from datetime import datetime

from Cliente import Cliente
from Producto import Producto
from Ventas import Ventas

# Clase principal Tienda, gestiona todo el control del programa y que tiene la mayoria de las funciones del mismo
class Tienda:
	def __init__(self):
		self.productos = []
		self.clientes = []
		self.ventas = []
	
		self.cargar_datos() # Funcion inicializadora del programa

	def cargar_datos(self): # Funcion que se encarga de cargar los datos desde la API
		url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"
		response = requests.get(url)

		if response.status_code == 200: # Extraccion de los datos desde el archivo .json de la API
			data = response.json()
			for item in data:
				producto = Producto(item["id"], item["name"], item["description"], item["price"], item["category"], item["inventory"], item["compatible_vehicles"])
				self.productos.append(producto)
		else:	
			print("Error al cargar los datos")

# Funciones que pertenecen a la Clase principal Tienda

	def agregar_producto(self, name, description, price, category, inventory, compatible_vehicles): # Funcion que sirve para agregar un nuevo producto a la tienda
		new_id = len(self.productos) + 1
		new_producto = Producto(new_id, name, description, price, category, inventory, compatible_vehicles)
		self.productos.append(new_producto) # Agregar nuevo producto
		print(f"Producto '{name}' agregado con éxito.")


	def buscar_productos(self, categoria=None, precio=None, nombre=None, disponibilidad=None): # Buscar un producto segun el filtro especificado
		resultados = []
		for producto in self.productos:
			if (categoria is None or producto.category == categoria) and \
				(precio is None or producto.price == precio) and \
				(nombre is None or producto.name.lower() == nombre.lower()) and \
				(disponibilidad is None or producto.inventory >= disponibilidad):
				resultados.append(producto)
		return resultados

	def buscar_producto_por_id(self, producto_id): # Buscar un producto especificamente por el id, es una funcion auxiliar para facilitar la busqueda
		for producto in self.productos:
			if producto.id == producto_id:
				return producto
		return None

	# Funcion que modifica un atributo de los productos, se especifica cual producto se deseas modificar
	def modificar_producto(self, producto_id, name=None, description=None, price=None, category=None, inventory=None, compatible_vehicles=None):
		producto = self.buscar_producto_por_id(producto_id)
		if producto:
			if name:
				producto.name = name
			if description:
				producto.description = description
			if price:
				producto.price = price
			if category:
				producto.category = category
			if inventory:
				producto.inventory = inventory
			if compatible_vehicles:
				producto.compatible_vehicles = compatible_vehicles if isinstance(compatible_vehicles, list) else [compatible_vehicles]
			print(f"Información de producto '{producto.name}' modificada con éxito.")
		else:
			print(f"No se encontró ningún producto con el ID '{producto_id}'.")

	def eliminar_producto(self, producto_id): # Eliminar un producto especificado de la tienda
		producto = self.buscar_producto_por_id(producto_id)
		if producto:
			self.productos.remove(producto) # Eliminacion del producto
			print(f"Producto '{producto.name}' eliminado con éxito.")
		else:
			print(f"No se encontró ningún producto con el ID '{producto_id}'.")

	# Funcion para registrar un nuevo cliente a la tienda
	def registrar_cliente(self, nombre, apellido, cedula_rif, correo, direccion, telefono, es_juridico=False, nombre_contacto=None, telefono_contacto=None, correo_contacto=None):
		nuevo_cliente = Cliente(nombre, apellido, cedula_rif, correo, direccion, telefono, es_juridico, nombre_contacto, telefono_contacto, correo_contacto)
		self.clientes.append(nuevo_cliente)
		tipo_cliente = "Cliente Jurídico" if es_juridico else "Cliente Natural"
		print(f"{tipo_cliente} '{nombre} {apellido}' registrado con éxito.")

	def modificar_cliente(self, cedula_rif, **kwargs): # Funcion para modificar cualquier atributo del cliente, exceptuando nombre, apellido y cedula
		cliente_encontrado = None
		for cliente in self.clientes:
			if cliente.cedula_rif == cedula_rif:
				cliente_encontrado = cliente
				break
        
		if cliente_encontrado:
			for key, value in kwargs.items():
				if hasattr(cliente_encontrado, key):
					setattr(cliente_encontrado, key, value)
			print(f"Información del cliente '{cliente_encontrado.nombre} {cliente_encontrado.apellido}' modificada con éxito.")
		else:
			print(f"No se encontró ningún cliente con la cédula/RIF '{cedula_rif}'.")


	def eliminar_cliente(self, cedula_rif): # Elimina un cliente que ya este registrado en la tienda mediante su cedula/rif
		cliente_encontrado = None
		for cliente in self.clientes:
			if cliente.cedula_rif == cedula_rif:
				cliente_encontrado = cliente
				break
        
		if cliente_encontrado:
			self.clientes.remove(cliente_encontrado)
			print(f"Cliente '{cliente_encontrado.nombre} {cliente_encontrado.apellido}' eliminado con éxito.")
		else:
			print(f"No se encontró ningún cliente con la cédula/RIF '{cedula_rif}'.")

	def buscar_clientes(self, cedula_rif=None, correo=None): # Funcion que busca a un cliente registrado en la tienda mediante su cedula/rif o correo
		resultados = []
		for cliente in self.clientes:
			if (cedula_rif is not None and cliente.cedula_rif == cedula_rif) or \
				(correo is not None and cliente.correo == correo):
				resultados.append(cliente)
		return resultados

	# Funcion que sirve para registrar una venta realizada en la tienda
	def registrar_venta(self, cliente, productos, cantidades, metodo_pago, metodo_envio, subtotal, descuentos, iva, igtf):
		total = subtotal - descuentos + (subtotal * iva) + (subtotal * igtf)
		nueva_venta = Ventas(cliente, productos, cantidades, metodo_pago, metodo_envio, subtotal, descuentos, subtotal * iva, subtotal * igtf, total)
		self.ventas.append(nueva_venta)
		print("Venta registrada exitosamente.")

	def buscar_ventas(self, cliente=None, fecha=None): # Funcion que se encarga de buscar ventas hechas en la tienda
		resultados = []
		for venta in self.ventas:
			if (cliente is None or venta.cliente == cliente) and (fecha is None or venta.fecha == fecha):
				resultados.append(venta)
		return resultados


	def generar_informe_ventas(self): # Funcion que genera un informe de las ventas de la tienda
		# Obtener la fecha actual
		today = datetime.now()

		# Filtrar ventas por año, mes, semana y día
		ventas_anio = [venta for venta in self.ventas if venta.fecha.year == today.year]
		ventas_mes = [venta for venta in ventas_anio if venta.fecha.month == today.month]
		ventas_semana = [venta for venta in ventas_mes if venta.fecha.isocalendar()[1] == today.isocalendar()[1]]
		ventas_dia = [venta for venta in ventas_semana if venta.fecha.day == today.day]

		# Calcular total de ventas para cada periodo
		total_ventas_anio = sum(venta.total for venta in ventas_anio)
		total_ventas_mes = sum(venta.total for venta in ventas_mes)
		total_ventas_semana = sum(venta.total for venta in ventas_semana)
		total_ventas_dia = sum(venta.total for venta in ventas_dia)

		# Encontrar los productos más vendidos
		productos_vendidos = [producto for venta in self.ventas for producto in venta.productos]
		productos_mas_vendidos = Counter(productos_vendidos).most_common(3)  # Obtener los 3 productos más vendidos

		# Encontrar los clientes más frecuentes
		clientes_ventas = [venta.cliente for venta in self.ventas]
		clientes_frecuentes = Counter(clientes_ventas).most_common(3)  # Obtener los 3 clientes más frecuentes

		return {
			"Fecha": today.strftime("%Y-%m-%d"),
			"Ventas Totales por Año": total_ventas_anio,
			"Ventas Totales por Mes": total_ventas_mes,
			"Ventas Totales por Semana": total_ventas_semana,
			"Ventas Totales por Día": total_ventas_dia,
			"Productos Más Vendidos": productos_mas_vendidos,
			"Clientes Más Frecuentes": clientes_frecuentes
		}

	def generar_informe_pagos(self): # Funcion que genera un informe de pagos de la tienda
		# Obtener la fecha actual
		today = datetime.now()

		# Filtrar pagos por año, mes, semana y día
		pagos_anio = [pago for pago in self.pagos if pago.fecha.year == today.year]
		pagos_mes = [pago for pago in pagos_anio if pago.fecha.month == today.month]
		pagos_semana = [pago for pago in pagos_mes if pago.fecha.isocalendar()[1] == today.isocalendar()[1]]
		pagos_dia = [pago for pago in pagos_semana if pago.fecha.day == today.day]

		# Calcular total de pagos para cada periodo
		total_pagos_anio = sum(pago.monto for pago in pagos_anio)
		total_pagos_mes = sum(pago.monto for pago in pagos_mes)
		total_pagos_semana = sum(pago.monto for pago in pagos_semana)
		total_pagos_dia = sum(pago.monto for pago in pagos_dia)

		# Encontrar clientes con pagos pendientes
		clientes_con_pagos_pendientes = [pago.cliente for pago in self.pagos if not pago.pagado]

		return {
			"Fecha": today.strftime("%Y-%m-%d"),
			"Pagos Totales por Año": total_pagos_anio,
			"Pagos Totales por Mes": total_pagos_mes,
			"Pagos Totales por Semana": total_pagos_semana,
			"Pagos Totales por Día": total_pagos_dia,
			"Clientes con Pagos Pendientes": list(set(clientes_con_pagos_pendientes))
		}


	def generar_informe_envios(self): # Funcion que genera un informe de los envios realizados de la tienda
		# Obtener la fecha actual
		today = datetime.now()

		# Filtrar envíos por año, mes, semana y día
		envios_anio = [envio for envio in self.envios if envio.fecha.year == today.year]
		envios_mes = [envio for envio in envios_anio if envio.fecha.month == today.month]
		envios_semana = [envio for envio in envios_mes if envio.fecha.isocalendar()[1] == today.isocalendar()[1]]
		envios_dia = [envio for envio in envios_semana if envio.fecha.day == today.day]

		# Calcular total de envíos para cada periodo
		total_envios_anio = len(envios_anio)
		total_envios_mes = len(envios_mes)
		total_envios_semana = len(envios_semana)
		total_envios_dia = len(envios_dia)

		# Encontrar los productos más enviados
		productos_enviados = [producto for envio in self.envios for producto in envio.productos]
		productos_mas_enviados = Counter(productos_enviados).most_common(3)  # Obtener los 3 productos más enviados

		# Encontrar clientes con envíos pendientes
		clientes_con_envios_pendientes = [envio.cliente for envio in self.envios if not envio.entregado]

		return {
			"Fecha": today.strftime("%Y-%m-%d"),
			"Envíos Totales por Año": total_envios_anio,
			"Envíos Totales por Mes": total_envios_mes,
			"Envíos Totales por Semana": total_envios_semana,
			"Envíos Totales por Día": total_envios_dia,
			"Productos Más Enviados": productos_mas_enviados,
			"Clientes con Envíos Pendientes": list(set(clientes_con_envios_pendientes))
		}

	def guardar_estado(self): # Funcion que genera un archivo .json con el estado de los clientes registrados y los productos existentes en la tienda
		ruta_actual = os.path.dirname(os.path.abspath(__file__))
		archivo = os.path.join(ruta_actual, "guardar_tienda.json")
		estado = {
			"productos": [producto.__dict__ for producto in self.productos],
			"clientes": [cliente.__dict__ for cliente in self.clientes]
		}

		with open(archivo, "w") as file:
			json.dump(estado, file, indent=4)

	def registrar_pago_usuario(self): # Funcion auxiliar para registrar un pago por el usuario
		# Solicitar al usuario los datos para el pago
		cliente = input("Ingrese cedula/rif del cliente: ")
		monto = float(input("Ingrese el monto: "))
		moneda = input("Ingrese la moneda: ")
		tipo_pago = input("Ingrese el tipo de pago: ")
		fecha = input("Ingrese la fecha (formato YYYY-MM-DD): ")

		# Buscar al cliente en la lista de clientes de la tienda
		cliente_encontrado = None
		for cli in self.clientes:
			if cli.cedula_rif == cliente:
				cliente_encontrado = cli
				break

		if cliente_encontrado:
			# Registrar el pago
			nueva_venta = Ventas(cliente, [], [], tipo_pago, "", 0, 0, 0, 0, 0)
			nueva_venta.registrar_pago(cliente, monto, moneda, tipo_pago, fecha)
		else:
			print("Cliente no encontrado. No se puede registrar el pago.")


	def generar_factura_usuario(self, clientes): # Funcion auxiliar para generar las facturas por el usuario
		# Solicitar al usuario los datos para la factura
		cliente = input("Ingrese el cliente: ")

		# Crear una venta ficticia para generar la factura
		nueva_venta = Ventas(cliente, [], [], "", "", 0, 0, 0, 0, 0)
		nueva_venta.generar_factura(clientes)


