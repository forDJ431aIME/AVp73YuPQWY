# 代码生成时间: 2025-08-25 08:39:12
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# 定义一个函数来格式化API响应
def format_api_response(response):
    try:
        # 尝试将响应解析成JSON格式
        response_json = json.loads(response)
        return json.dumps(response_json, indent=4)
    except json.JSONDecodeError:
        # 如果解析失败，返回原始响应
        return response

# 创建一个Kivy应用
class ApiResponseFormatterApp(App):
    def build(self):
        # 创建一个布局
        layout = BoxLayout(orientation='vertical')

        # 创建一个输入框，用于输入API响应
        self.input_text = TextInput(multiline=True,
                                 size_hint_y=None,
                                 height=200)
        layout.add_widget(self.input_text)

        # 创建一个按钮，用于触发格式化操作
        self.format_button = Button(text='Format Response')
        self.format_button.bind(on_press=self.format_response)
        layout.add_widget(self.format_button)

        # 创建一个标签，用于显示格式化后的响应
        self.output_label = Label(text='',
                                 text_size=(Window.width, None),
                                 size_hint_y=None,
                                 height=200)
        layout.add_widget(self.output_label)

        return layout

    def format_response(self, instance):
        # 获取输入框中的API响应
        raw_response = self.input_text.text
        # 格式化API响应
        formatted_response = format_api_response(raw_response)
        # 更新输出标签的文本
        self.output_label.text = formatted_response

# 运行Kivy应用
if __name__ == '__main__':
    ApiResponseFormatterApp().run()