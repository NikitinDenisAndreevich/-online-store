import pytest

from models import Product, Category


@pytest.fixture(autouse=True)
def reset_counters():
	# Ensure each test starts with clean counters
	Category.category_count = 0
	Category.product_count = 0
	yield
	# Clean up not strictly necessary here


def test_product_initialization():
	product = Product("Test Phone", "Desc", 1000.0, 3)
	assert product.name == "Test Phone"
	assert product.description == "Desc"
	assert product.price == 1000.0
	assert product.quantity == 3


def test_category_initialization_and_products_list():
	p1 = Product("A", "a", 10.0, 1)
	p2 = Product("B", "b", 20.0, 2)
	category = Category("Phones", "All phones", [p1, p2])
	assert category.name == "Phones"
	assert category.description == "All phones"
	assert isinstance(category.products, list)
	assert category.products == [p1, p2]


def test_counters_increment_on_category_creation():
	p1 = Product("A", "a", 10.0, 1)
	p2 = Product("B", "b", 20.0, 2)
	Category("Phones", "All phones", [p1, p2])
	assert Category.category_count == 1
	assert Category.product_count == 2


def test_counters_accumulate_across_multiple_categories():
	p1 = Product("A", "a", 10.0, 1)
	p2 = Product("B", "b", 20.0, 2)
	p3 = Product("C", "c", 30.0, 3)
	Category("Phones", "All phones", [p1, p2])
	Category("Tablets", "All tablets", [p3])
	assert Category.category_count == 2
	assert Category.product_count == 3
