# E-commerce System with Users, Products, and Admin

This Python script simulates a simple e-commerce system where 
users can add products to their cart, view products, and place orders. 
Administrators can manage the product list by adding and removing products.

## Project Description

The system is built around two main classes: Product and User, 
with an additional Admin class inheriting from User. Here’s an overview 
of the classes and their functionality:

### Classes
1. **Product:**
    - Represents a product with a name, price, and description.
    - Keeps a list of all available products in the system.
    - Provides methods to:
        - Create a product.
        - Calculate the total price of a list of products.
2. **User:**
    - Represents a user who can add products to a shopping cart, view their cart, and place orders.
    - Provides methods to:
        - Add products to the cart.
        - Remove products from the cart.
        - View the cart contents.
        - Place orders and clear the cart.
        - View user information and previous orders.
3. **Admin (inherits from User):**
    - In addition to the functionality of a regular user, the `Admin` can:
        - Add products to the system.
        - Remove products from the system.
        - View all available products in the system.

### Key Functions

`Product`
- `create(name: str, price: float, description: str) -> Product`:
Creates a new product with the specified name, price (rounded to 2 decimal places), and description.
- `objects() -> List[Product]`: Returns a list of all products in the system.
- `calculate_total(products: List[Product]) -> float`: Calculates the total price of a list of products.

`User`
- `add_to_cart(product: Product)`: Adds a product to the user's cart if it is available.
- `remove_from_cart(product: Product)`: Removes a product from the user's cart.
- `view_cart() -> str`: Returns a string with all product names currently in the cart.
- `place_order()`: Places an order for all products in the cart and clears the cart.
- `about_me()`: Prints information about the user, their cart, and their previous orders.
- `show_products(products: List[Product])`: Displays available and unavailable products from the given list.

`Admin`
- `add_product(product: Product)`: Adds a product to the system's product list.
- `remove_product(product: Product)`: Removes a product from the system's product list.
- `show_products()`: Displays all products currently available in the system.

### Example Usage

Here’s how you can use the script to simulate user and admin actions:
```python
# Creating products
mouse = Product.create("mouse", 124.134134, "black")
laptop = Product.create("laptop", 1234.124256, "black")
phone = Product.create("phone", 1232.1234515, "blue")

# Creating an admin and adding products
admin = Admin.create("admin", "admin@email.com")
admin.add_product(mouse)
admin.add_product(laptop)

# Creating a user and interacting with the cart
user = User.create("user", "user@gmail.com")
user.add_to_cart(laptop)
user.add_to_cart(mouse)
print(user.view_cart())

user.remove_from_cart(mouse)
print(user.view_cart())

user.place_order()
user.about_me()

# Viewing available and unavailable products
user.show_products([mouse, laptop, phone])

# Admin removes a product
admin.remove_product(mouse)
user.show_products([mouse, laptop, phone])

# Admin views all products
admin.show_products()

# Calculating total price of products
# total = Product.calculate_total([mouse, laptop, phone])
# print(f"Total price: {total}")

```

### License
This project is open-source and free to use.