from typing import List


class Product:
    __product_list: List['Product'] = []

    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = round(price, 2)
        self.description = description

    @classmethod
    def create(cls, name: str, price: float, description: str) -> 'Product':
        return cls(name, price, description)

    @classmethod
    def objects(cls) -> List['Product']:
        return cls.__product_list

    @staticmethod
    def calculate_total(products: List['Product']) -> float:
        total = sum(product.price for product in products)
        return round(total, 2)

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.cart: List['Product'] = []
        self.place_orders: List[str] = []

    @classmethod
    def create(cls, name: str, email: str) -> 'User':
        return cls(name, email)

    def add_to_cart(self, product: 'Product'):
        if product in self.cart and product not in Product._Product__product_list:
            print(f"Продукт уже в корзине или недоступен: {product.name}")
        else:
            self.cart.append(product)

    def remove_from_cart(self, product: 'Product'):
        if product not in self.cart:
            print(f"Продукта нет в корзине: {product.name}")
        else:
            self.cart.remove(product)

    def view_cart(self) -> str:
        view_cart = ', '.join(product.name for product in self.cart)
        return view_cart

    def place_order(self):
        print(f"Ваша корзина: {self.view_cart()}")
        print(f"Заказы оформлены: {self.view_cart()}")
        self.place_orders.append(f"Оформленные заказы: {self.view_cart()}")
        self.cart.clear()
        print(f"Ваша корзина: {self.view_cart()}")

    def about_me(self):
        print(f"Ваша имя: {self.name}, Ваш email: {self.email}")
        print(f"Ваша корзина: {self.view_cart()}")
        place_orders = '\n'.join(place_order for place_order in self.place_orders)
        print(place_orders)

    def show_products(self, products: List['Product']):
        available_products = []
        not_available_products = []
        products2 = Product._Product__product_list
        for product1 in products:
            if product1 in products2:
                available_products.append(product1.name)
            else:
                not_available_products.append(product1.name)
        print(f"Доступные продукты: {available_products}")
        print(f"Недоступные продукты: {not_available_products}")


class Admin(User):
    def add_product(self, product: 'Product'):
        if product in Product._Product__product_list:
            print(f"Продукт уже в системе: {product.name}")
        else:
            Product._Product__product_list.append(product)

    def remove_product(self, product: 'Product'):
        if product not in Product._Product__product_list:
            print(f"Продукта нету в системе: {product.name}")
        else:
            Product._Product__product_list.remove(product)

    def show_products(self):
        products = ', '.join(product.name for product in Product._Product__product_list)
        print(f"Список всех продуктов в системе: {products}")


mouse = Product.create("mouse", 124.134134, "black")
laptop = Product.create("laptop", 1234.124256, "black")
phone = Product.create("phone", 1232.1234515, "blue")

admin = Admin.create("admin", "admin@email.com")
admin.add_product(mouse)
admin.add_product(laptop)

user = User.create("user", "user@gmail.com")
user.add_to_cart(laptop)
user.add_to_cart(mouse)
print(user.view_cart())
user.remove_from_cart(mouse)
print(user.view_cart())

print()
user.place_order()

print()
user.about_me()

print()
user.show_products([mouse, laptop, phone])

admin.remove_product(mouse)
user.show_products([mouse, laptop, phone])

print()
admin.show_products()

# total = Product.calculate_total([mouse, laptop, phone])
# print(f"Общая сумма: {total}")