# 代码生成时间: 2025-09-23 01:01:39
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# 定义库存项类
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}
"

# 定义库存管理系统类
class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name].quantity >= quantity:
                self.items[item_name].quantity -= quantity
                if self.items[item_name].quantity <= 0:
                    del self.items[item_name]
            else:
                raise ValueError("Not enough quantity to remove.")
        else:
            raise ValueError("Item does not exist.")

# 定义Kivy界面类
class InventoryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.create_input_area())
        self.layout.add_widget(self.create_button_area())
        return self.layout

    def create_input_area(self):
        # 创建输入区域
        self.name_input = TextInput(hint_text='Item Name')
        self.quantity_input = TextInput(hint_text='Quantity')
        return BoxLayout(orientation='horizontal', size_hint_y=None, height=50).add_widgets(
            [self.name_input, self.quantity_input]
        )

    def create_button_area(self):
        # 创建按钮区域
        add_button = Button(text='Add')
        add_button.bind(on_press=self.add_item)
        remove_button = Button(text='Remove')
        remove_button.bind(on_press=self.remove_item)
        return BoxLayout(orientation='horizontal', size_hint_y=None, height=50).add_widgets(
            [add_button, remove_button]
        )

    def add_item(self, instance):
        try:
            item_name = self.name_input.text.strip()
            quantity = int(self.quantity_input.text.strip())
            if item_name and quantity > 0:
                self.manager.add_item(InventoryItem(item_name, quantity))
                self.show_message(f'Added {item_name} with quantity {quantity}')
                self.name_input.text = ''
                self.quantity_input.text = ''
            else:
                self.show_message('Invalid input')
        except ValueError as e:
            self.show_message(str(e))

    def remove_item(self, instance):
        try:
            item_name = self.name_input.text.strip()
            quantity = int(self.quantity_input.text.strip())
            if item_name and quantity > 0:
                self.manager.remove_item(item_name, quantity)
                self.show_message(f'Removed {quantity} of {item_name}')
                self.name_input.text = ''
                self.quantity_input.text = ''
            else:
                self.show_message('Invalid input')
        except ValueError as e:
            self.show_message(str(e))

    def show_message(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text=message, size_hint_y=None, height=50))
        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(200, 200))
        popup.open()

    def on_start(self):
        self.manager = InventoryManager()

# 运行应用
if __name__ == '__main__':
    InventoryApp().run()
