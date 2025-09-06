# 代码生成时间: 2025-09-06 08:42:19
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
import random

# 排序算法函数
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# UI类
class SortingApp(App):
    def build(self):
        # 创建布局
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # 创建输入框
        self.input_label = Label(text='Enter numbers separated by commas:', size_hint_y=None, height=30)
        self.number_input = TextInput(multiline=False, size_hint_y=None, height=30)

        # 创建排序算法选择下拉菜单
        self.sort_method_label = Label(text='Choose sorting method:', size_hint_y=None, height=30)
        self.sort_methods = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
        self.sort_method_dropdown = DropDown()
        for method in self.sort_methods:
            item = DropDownItem(text=method, on_press=lambda x: setattr(self, 'selected_sort_method', method))
            self.sort_method_dropdown.add_item(item)

        # 创建排序按钮
        self.sort_button = Button(text='Sort', size_hint_y=None, height=30)
        self.sort_button.bind(on_press=self.sort_numbers)

        # 创建结果显示区域
        self.result_label = Label(text='', size_hint_y=None, height=100)
        self.result_label.bind(size=self.update_label_size)

        # 将组件添加到布局中
        self.layout.add_widget(self.input_label)
        self.layout.add_widget(self.number_input)
        self.layout.add_widget(self.sort_method_label)
        self.layout.add_widget(self.sort_method_dropdown)
        self.layout.add_widget(self.sort_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def sort_numbers(self, instance):
        # 获取输入的数字字符串
        numbers_str = self.number_input.text

        # 处理错误输入
        try:
            numbers = [int(num.strip()) for num in numbers_str.split(',')]
        except ValueError:
            self.show_error_popup('Invalid input. Please enter numbers separated by commas.')
            return

        # 根据选择的方法进行排序
        if self.selected_sort_method == 'Bubble Sort':
            bubble_sort(numbers)
        elif self.selected_sort_method == 'Selection Sort':
            selection_sort(numbers)
        elif self.selected_sort_method == 'Insertion Sort':
            insertion_sort(numbers)
        else:
            self.show_error_popup('No sorting method selected.')
            return

        # 显示排序结果
        self.result_label.text = 'Sorted numbers: ' + ', '.join(map(str, numbers))

    def update_label_size(self, instance, value):
        instance.text_size = (instance.width, None)
        return instance.text_size

    def show_error_popup(self, message):
        # 创建错误提示弹窗
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# 运行应用
if __name__ == '__main__':
    SortingApp().run()