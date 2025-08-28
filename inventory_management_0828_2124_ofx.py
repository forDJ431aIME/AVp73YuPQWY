# 代码生成时间: 2025-08-28 21:24:38
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

# 定义一个简单的库存项模型
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

# 库存管理界面
class InventoryManagement(BoxLayout):
    def __init__(self, **kwargs):
        super(InventoryManagement, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Inventory Management System"))

        self.item_list = []  # 用于存储库存项的列表

        # 创建输入框和按钮
        self.add_widget(Label(text="Item Name"))
        self.item_name_input = TextInput(multiline=False)
        self.add_widget(self.item_name_input)

        self.add_widget(Label(text="Quantity"))
        self.quantity_input = TextInput(multiline=False)
        self.add_widget(self.quantity_input)

        self.add_widget(Button(text="Add Item", on_press=self.add_item))

        # 显示库存列表
        self.inventory_display = Label(text="")
        self.add_widget(self.inventory_display)

    def add_item(self, instance):
        """添加库存项到列表"""
        item_name = self.item_name_input.text.strip()
        quantity = self.quantity_input.text.strip()

        if not item_name or not quantity:
            self.show_error_popup("You must enter both item name and quantity.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.show_error_popup("Quantity must be an integer.")
            return

        self.item_list.append(InventoryItem(item_name, quantity))
        self.update_inventory_display()

    def update_inventory_display(self):
        """更新库存显示"""
        inventory_text = "
".join([f"{item.name}: {item.quantity}" for item in self.item_list])
        self.inventory_display.text = inventory_text

    def show_error_popup(self, message):
        """显示错误信息的弹出窗口"""
        popup = Popup(title="Error", content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# 定义Kivy应用
class InventoryApp(App):
    def build(self):
        return InventoryManagement()

# 运行应用
if __name__ == '__main__':
    InventoryApp().run()