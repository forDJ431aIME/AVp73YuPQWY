# 代码生成时间: 2025-09-06 01:43:43
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

# 商品类
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - ${self.price}"

# 购物车类
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product} to cart")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Removed {product} from cart")
        else:
            print("Product not found in cart")

    def get_total_price(self):
        return sum(product.price for product in self.products)

# 购物车主屏幕
class ShoppingCartScreen(Screen):
    def __init__(self, **kwargs):
        super(ShoppingCartScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.cart = ShoppingCart()

        self.product_dropdown = DropDown()
        self.product_dropdown_pos = 10
        self.populate_product_dropdown()
        self.product_dropdown.bind(on_select=self.on_product_select)
        self.layout.add_widget(self.product_dropdown)

        self.add_button = Button(text="Add to Cart")
        self.add_button.bind(on_press=self.add_to_cart)
        self.layout.add_widget(self.add_button)

        self.cart_label = Label(text="Your cart is empty")
        self.layout.add_widget(self.cart_label)

    def populate_product_dropdown(self):
        # 假设的商品列表
        products = [Product("Apple", 0.99), Product("Banana", 0.59), Product("Carrot", 0.29)]
        for product in products:
            self.product_dropdown.add_item(
                Label(text=product.__repr__()),
                Product(product.name, product.price)
            )

    def on_product_select(self, instance, value):
        self.current_product = value

    def add_to_cart(self, instance):
        if self.current_product:
            self.cart.add_product(self.current_product)
            self.update_cart_label()
        else:
            print("Please select a product")

    def update_cart_label(self):
        total_price = self.cart.get_total_price()
        if self.cart.products:
            product_names = ', '.join([f"{product.name}" for product in self.cart.products])
            self.cart_label.text = f"Products in cart: {product_names} - Total: ${total_price:.2f}"
        else:
            self.cart_label.text = "Your cart is empty"

# Kivy应用类
class ShoppingCartApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ShoppingCartScreen(name="cart"))
        return sm

if __name__ == "__main__":
    ShoppingCartApp().run()