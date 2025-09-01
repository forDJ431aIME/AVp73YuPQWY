# 代码生成时间: 2025-09-02 04:23:28
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

"""
随机数生成器程序
"""

class RandomNumberGeneratorApp(App):
    def build(self):
        # 创建布局
        layout = BoxLayout(orientation='vertical')

        # 创建标签显示随机数
        self.random_number_label = Label(text='随机数生成器')
        layout.add_widget(self.random_number_label)

        # 创建按钮，点击后生成随机数
        generate_button = Button(text='生成随机数')
        generate_button.bind(on_press=self.generate_random_number)
        layout.add_widget(generate_button)

        # 创建按钮，点击后复制随机数到剪贴板
        copy_button = Button(text='复制随机数')
        copy_button.bind(on_press=self.copy_random_number)
        layout.add_widget(copy_button)

        return layout

    def generate_random_number(self, instance):
        """
        生成随机数并在标签上显示
        """
        try:
            # 生成1到100之间的随机数
            random_number = random.randint(1, 100)
            self.random_number_label.text = f'随机数：{random_number}'
        except Exception as e:
            # 显示错误信息
            self.show_error_popup(f'生成随机数失败：{str(e)}')

    def copy_random_number(self, instance):
        """
        将当前随机数复制到剪贴板
        """
        try:
            import pyperclip
            pyperclip.copy(self.random_number_label.text.split('：')[-1])
        except Exception as e:
            # 显示错误信息
            self.show_error_popup(f'复制随机数失败：{str(e)}')

    def show_error_popup(self, error_message):
        """
        显示错误信息弹窗
        """
        popup = Popup(title='错误', content=Label(text=error_message), size_hint=(None, None), size=(200, 200))
        popup.open()


def run_app():
    RandomNumberGeneratorApp().run()

def main():
    run_app()

if __name__ == '__main__':
    main()
