class Product:
	def __init__(self, name: str, description: str, price: float, quantity: int):
		self.name = name
		self.description = description
		self.price = float(price)
		self.quantity = int(quantity)


class Category:
	# Class-level counters shared across all instances
	category_count: int = 0
	product_count: int = 0

	def __init__(self, name: str, description: str, products: list[Product]):
		self.name = name
		self.description = description
		self.products = list(products)

		# Update class-level counters
		Category.category_count += 1
		Category.product_count += len(self.products)
