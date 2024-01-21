from classes.store import Store
from classes.product import Product


shop = Store("Speed Up")

turbo = Product("Turbo",800,"engine_parts")
doorknob = Product("Doorknob",150,"accessory")
piston = Product("Piston",450,"engine_parts")
wheel = Product("Wheel",600,"accessory")

shop.add_product(turbo).add_product(doorknob).add_product(piston).add_product(wheel).store_info()
shop.sell_product(2).store_info()
shop.add_product(turbo).store_info()
shop.inflation(0.1).store_info()
shop.set_clearance("engine_parts",0.1).store_info()