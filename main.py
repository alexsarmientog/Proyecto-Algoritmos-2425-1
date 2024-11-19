from Tienda import Tienda

# Funcion principal del programa, se encuentra todo el flujo del mismo
def main():
	tienda = Tienda() # Instancia principal del programa 

	opcion = 0
	print("--- Tienda. Productos para vehículos ---") # Despliegue del menu con el que se interactua
	while(opcion != 17):
		print("**** BIENVENIDO ****\nMenu") # Lista de todas las opciones
		print("1. Agregar Prodcuto")
		print("2. Buscar Producto")
		print("3. Modificar Informacion de Producto")
		print("4. Eliminar Producto")
		print("5. Registrar Venta")
		print("6. Generar Factura de Compra")
		print("7. Buscar Ventas")
		print("8. Registrar Cliente")
		print("9. Modificar Informacion de Cliente")
		print("10. Eliminar Cliente")
		print("11. Buscar Cliente")
		print("12. Registrar Pago")
		print("13. Buscar Pago")
		print("14. Registrar Envio")
		print("15. Buscar Envio")
		print("16. Generar informes (Venta - Pagos - Envios)")
		print("17. Salir")
		opcion = int(input("\nElija una opcion: "))
		if opcion == 1:
			print("\nAgregar producto nuevo: ")
			name = input("Nombre: ")
			description = input("Descripcion: ")
			price = input("Precio: ")
			while True:
				while not price.isnumeric():
					print("El precio es un valor numerico, ingrese el valor nuevamente...")
					price = input("Precio: ")
				break
			category = input("Categoria: ")
			inventory = input("Inventario: ")
			compatible_vehicles = input("Vehículos compatibles (separados por coma): ").split(",")
			tienda.agregar_producto(name, description, price, category, inventory, compatible_vehicles)
		
		elif opcion == 2:
			op = 0		
			print("\n--> 1. Categoria\n--> 2. Precio\n--> 3. Nombre\n--> 4. Disponibilidad")
			op = int(input("Selecciona filtro: "))

			if op == 1:
				categoria = input("Categoria: ")
				resultado = tienda.buscar_productos(categoria=categoria)
				for producto in resultado:
					print(producto.name)
			elif op == 2:
				precio = float(input("Precio: "))
				resultado = tienda.buscar_productos(precio=precio)
				for producto in resultado:
					print(producto.name)
			elif op == 3:
				nombre = input("Nombre: ")
				resultado = tienda.buscar_productos(nombre=nombre)
				for producto in resultado:
					print(producto.name)
			elif op == 4:
				disponibilidad = int(input("Disponibilidad: "))
				resultado = tienda.buscar_productos(disponibilidad=disponibilidad)
				for producto in resultado:
					print(producto.name)
		
		elif opcion == 3:
			op = 0
			print("\n--> 1. Nombre\n--> 2. Descipcion\n--> 3. Precio\n--> 4.Categoria\n--> 5.Inventario\n--> 6.Vehiculos compatibles")
			op = int(input("Selecciona para modificar: "))
			id_producto = input("Coloca id del producto a modificar: ")

			if op == 1:
				nombre = input("Nuevo nombre: ")
				tienda.modificar_producto(id_producto, name=nombre)
			elif op == 2:
				descripcion = input("Nueva descripcion: ")
				tienda.modificar_producto(id_producto, description=descripcion)
			elif op == 3:
				precio = float(input("Nuevo precio: "))
				tienda.modificar_producto(id_producto, price=precio)
			elif op == 4:
				categoria = input("Nueva categoria: ")
				tienda.modificar_producto(id_producto, category=categoria)
			elif op == 5:
				inventario = int(input("Nuevo inventario: "))
				tienda.modificar_producto(id_producto, inventory=inventario)
			elif op == 6:
				vehiculos = input("Nuevos vehículos compatibles (separados por coma): ").split(",")
				tienda.modificar_producto(id_producto, compatible_vehicles=vehiculos)
		
		elif opcion == 4:
			id_producto = input("\nProducto a eliminar (id): ")
			tienda.eliminar_producto(id_producto)
		
		elif opcion == 5:
			print("\nRegistrar venta: ")
			cliente = input("Cedula/Rif cliente: ")
			productos = input("Productos (separados por coma): ").split(",")
			cantidad = input("Cantidad de cada producto (separados por coma)").split(",")
			metodo_pago = input("Metodo de pago: ")
			metodo_envio = input("Metodo de envio: ")
			subtotal = float(input("Subtotal: "))
			descuento = float(input("Coloque 0.05 si es juridico (0.0 dlc): "))
			iva = float(input("Coloque 0.16: "))
			igtf = float(input("Coloque 0.03 si paga en divisas (0.0 dlc): "))
			tienda.registrar_venta(cliente, productos, cantidad, metodo_pago, metodo_envio, subtotal, descuento, iva, igtf)

		elif opcion == 6:
			lista_clientes = tienda.clientes
			tienda.generar_factura_usuario(lista_clientes)

		elif opcion == 7:
			op = 0
			print("\n--> 1. Cliente\n--> 2. Fecha")
			op = int(input("Seleccione filtro: "))

			if op == 1:
				nombre = input("Nombre del cliente: ")
				resultado = tienda.buscar_ventas(cliente=nombre)
				for venta in resultado:
					print(f"Cliente: {venta.cliente}, Total: {venta.total}")
			elif op == 2:
				fecha = input("Fecha (aaaa, mm, dd): ")
				resultado = tienda.buscar_ventas(fecha=fecha)
				for venta in resultado:
					print(f"Cliente: {venta.cliente}, Total: {venta.total}")

		elif opcion == 8:
			print("\nDatos del Cliente: ")
			nombre = input("Nombre: ")
			apellido = input("Apellido: ")
			cedula_rif = input("Cedula (V0000 Persona Natural - J0000 Persona Juridica): ")
			correo = input("Correo: ")
			direccion = input("Direccion: ")
			telefono = input("Telefono: ")
			es_juridico = input("Coloque True si es juridico, False de lo contrario: ")
			if es_juridico.lower() == "true":
				es_juridico = True
				nombre_contacto = input("Nombre de contacto: ")
				telefono_contacto = input("Telefono de contacto: ")
				correo_contacto = input("Correo de contacto: ")
				tienda.registrar_cliente(nombre, apellido, cedula_rif, correo, direccion, telefono, es_juridico, nombre_contacto, telefono_contacto, correo_contacto)
			else:
				es_juridico = False
				tienda.registrar_cliente(nombre, apellido, cedula_rif, correo, direccion, telefono)
				
		elif opcion == 9:
			cedula_rif = input("\nCedula/Rif del Cliente a modificar: ")
			op = 0
			print("\n--> 1. Correo\n--> 2. Direccion\n--> 3. Telefono")
			op = int(input("Seleccione filtro: "))
			if op == 1:
				correo = input("Nuevo correo: ")
				tienda.modificar_cliente(cedula_rif, correo)
			elif op == 2:
				direccion = input("Nueva direccion: ")
				tienda.modificar_cliente(cedula_rif, direccion)
			elif op == 3:
				telefono = input("Nuevo telefono: ")
				tienda.modificar_cliente(cedula_rif, telefono)

		elif opcion == 10:
			cedula_rif = input("\nCedula/Rif del Cliente a eliminar: ")
			tienda.eliminar_cliente(cedula_rif)

		elif opcion == 11:
			op = 0
			print("\n--> 1. Cedula/Rif\n--> 2. Correo")
			op = int(input("Seleccione filtro: "))
			if op == 1:
				cedula_rif = input("Ingrese cedula/rif para buscar: ")
				resultado = tienda.buscar_clientes(cedula_rif=cedula_rif)
				for cliente in resultado:
					print(f"{cliente.nombre}, {cliente.apellido}")
			elif op == 2:
				correo = input("Ingrese correo para buscar: ")
				resultado = tienda.buscar_clientes(correo=correo)
				for cliente in resultado:
					print(f"{cliente.nombre}, {cliente.apellido}")

		elif opcion == 12:
			tienda.registrar_pago_usuario()

		elif opcion == 13:
			op = 0
			print("\n--> 1. Cliente\n--> 2. Fecha\n--> 3. Tipo de pago\n--> 4. Moneda")
			op = int(input("Seleccione filtro: "))
			if op == 1:
				resultado = []
				cliente = input("Ingrese cedula/rif del cliente: ")
				for venta in tienda.ventas:
					pagos = venta.buscar_pagos(cliente=cliente)
					resultado.extend(pagos)
				for pago in resultado:
					print(f"Cliente: {pago.cliente}")
					print(f"Monto: {pago.monto}")
					print(f"Moneda: {pago.moneda}")
					print(f"Tipo de Pago: {pago.tipo_pago}")
					print(f"Fecha: {pago.fecha}")
					print("-------------")

			elif op == 2:
				resultado = []
				fecha = input("Ingrese fecha (aaaa-mm-dd): ")
				for venta in tienda.ventas:
					pagos = venta.buscar_pagos(fecha=fecha)
					resultado.extend(pagos)

				for pago in resultado:
					print(f"Cliente: {pago.cliente}")
					print(f"Monto: {pago.monto}")
					print(f"Moneda: {pago.moneda}")
					print(f"Tipo de Pago: {pago.tipo_pago}")
					print(f"Fecha: {pago.fecha}")
					print("-------------")

			elif op == 3:
				resultado = []
				tipo_pago = input("Tipo de pago: ")
				for venta in tienda.ventas:
					pagos = venta.buscar_pagos(tipo_pago=tipo_pago)
					resultado.extend(pagos)

				for pago in resultado:
					print(f"Cliente: {pago.cliente}")
					print(f"Monto: {pago.monto}")
					print(f"Moneda: {pago.moneda}")
					print(f"Tipo de Pago: {pago.tipo_pago}")
					print(f"Fecha: {pago.fecha}")
					print("-------------")

			elif op == 4:
				resultado = []
				moneda = input("Moneda: ")
				for venta in tienda.ventas:
					pagos = venta.buscar_pagos(moneda=moneda)
					resultado.extend(pagos)

				for pago in resultado:
					print(f"Cliente: {pago.cliente}")
					print(f"Monto: {pago.monto}")
					print(f"Moneda: {pago.moneda}")
					print(f"Tipo de Pago: {pago.tipo_pago}")
					print(f"Fecha: {pago.fecha}")
					print("-------------")

		elif opcion == 14:
			print("\nRegistrar la orden de compra: ")
			orden = input("Orden de compra: ")
			servicio_envio = input("Servicio de envio: ")
			motorizado = input("Nombre del motorizado (en caso de solicitar delivery): ")
			costo_servicio = float(input("Costo del servicio: "))
			tienda.ventas.registrar_envio(orden, servicio_envio, motorizado, costo_servicio)

		elif opcion == 15:
			op = 0
			print("\n--> 1. Cliente\n--> 2. Fecha")
			op = int(input("Seleccione filtro: "))
			if op == 1:
				resultado = []
				cliente = input("Cedula/rif del cliente: ")
				for venta in tienda.ventas:
					envios = venta.buscar_envios(cliente=cliente)
					resultado.extend(envios)

				for envio in resultado:
					print(f"Orden de compra: {envio.orden_compra}")
					print(f"Servicio de envio: {servicio_envio}")
					print(f"Costo de servicio: {costo_servicio}")

			elif op == 2:
				resultado = []
				fecha = input("Ingrese la fecha del envio (aaaa-mm-dd): ")
				for venta in tienda.ventas:
					envios = venta.buscar_envios(fecha=fecha)
					resultado.extend(envios)

				for envio in resultado:
					print(f"Orden de compra: {envio.orden_compra}")
					print(f"Servicio de envio: {servicio_envio}")
					print(f"Costo de servicio: {costo_servicio}")
	
		elif opcion == 16:
			tienda.generar_informe_pagos()
			tienda.generar_informe_envios()
			tienda.generar_informe_ventas()

		elif opcion == 17:
			tienda.guardar_estado()
			print("Saliendo de la Tienda")

		else:
			print("Opcion incorrecta")
main() # Funcion principal, para ejecutar el programa