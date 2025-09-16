# 代码生成时间: 2025-09-16 11:19:56
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import json
import os

"""
库存管理系统
"""
class InventoryManagementApp(App):
    def build(self):
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical')

        # 创建显示库存的标签
        self.inventory_label = Label(text='Inventory:', size_hint_y=None, height=30)
        self.layout.add_widget(self.inventory_label)

        # 创建显示库存数据的文本框
        self.inventory_text = TextInput(multiline=True, readonly=True, size_hint_y=0.5)
        self.layout.add_widget(self.inventory_text)

        # 创建保存按钮
        save_button = Button(text='Save Inventory', size_hint_y=None, height=30)
        save_button.bind(on_press=self.save_inventory)
        self.layout.add_widget(save_button)

        # 创建加载按钮
        load_button = Button(text='Load Inventory', size_hint_y=None, height=30)
        load_button.bind(on_press=self.load_inventory)
        self.layout.add_widget(load_button)

        # 创建添加物品按钮
        add_item_button = Button(text='Add Item', size_hint_y=None, height=30)
        add_item_button.bind(on_press=self.add_item)
        self.layout.add_widget(add_item_button)

        return self.layout

    def save_inventory(self, instance):
        """保存库存数据到文件"""
        try:
            # 读取文本框内容并保存到文件
            with open('inventory.json', 'w') as file:
                json.dump(json.loads(self.inventory_text.text), file, indent=4)
        except json.JSONDecodeError:
            # 弹出错误提示
            self.show_error_popup('Invalid JSON format.')
        except Exception as e:
            self.show_error_popup(str(e))

    def load_inventory(self, instance):
        """从文件加载库存数据"""
        try:
            # 读取文件内容并显示在文本框
            with open('inventory.json', 'r') as file:
                self.inventory_text.text = json.dumps(json.load(file), indent=4)
        except FileNotFoundError:
            self.show_error_popup('Inventory file not found.')
        except json.JSONDecodeError:
            self.show_error_popup('Invalid JSON format in file.')
        except Exception as e:
            self.show_error_popup(str(e))

    def add_item(self, instance):
        """添加一个新物品到库存"""
        # 弹出输入框让用户输入新物品的名称和数量
        self.item_name = TextInput(text='', hint_text='Item Name', multiline=False)
        self.item_quantity = TextInput(text='', hint_text='Item Quantity', multiline=False)

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Add a new item:'))
        content.add_widget(self.item_name)
        content.add_widget(self.item_quantity)

        popup = Popup(title='Add Item', content=content, size_hint=(0.9, 0.9))
        popup.bind(on_dismiss=self.add_item_to_inventory)
        popup.open()

    def add_item_to_inventory(self, instance):
        """将新物品添加到库存"""
        try:
            # 获取用户输入的新物品信息
            item_name = self.item_name.text.strip()
            item_quantity = int(self.item_quantity.text.strip())

            # 加载当前库存数据
            inventory = json.loads(self.inventory_text.text)

            # 添加新物品到库存
            if item_name in inventory:
                inventory[item_name] += item_quantity
            else:
                inventory[item_name] = item_quantity

            # 更新文本框内容
            self.inventory_text.text = json.dumps(inventory, indent=4)
        except ValueError:
            self.show_error_popup('Invalid item quantity.')
        except json.JSONDecodeError:
            self.show_error_popup('Invalid JSON format.')
        except Exception as e:
            self.show_error_popup(str(e))

    def show_error_popup(self, error_message):
        """显示错误提示"""
        popup = Popup(title='Error', content=Label(text=error_message), size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    InventoryManagementApp().run()