# Clase Producto, con sus atributos respectivos
class Producto:
    def __init__(self, id, name, description, price, category, inventory, compatible_vehicles):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.inventory = inventory
        self.compatible_vehicles = compatible_vehicles if isinstance(compatible_vehicles, list) else [compatible_vehicles]
