# 代码生成时间: 2025-08-19 19:10:01
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

"""
API响应格式化工具，用于转换和美化API响应数据
"""


class ApiResponseFormatterApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')

        # 创建输入框，用于输入API响应数据
        self.response_input = TextInput(multiline=True, size_hint_y=None, height=200)
        layout.add_widget(self.response_input)

        # 创建格式化按钮
        format_button = Button(text='格式化')
        format_button.bind(on_press=self.format_response)
        layout.add_widget(format_button)

        # 创建输出框，用于显示格式化后的数据
        self.formatted_output = Label(text='', size_hint_y=None, height=200)
        layout.add_widget(self.formatted_output)

        return layout

    def format_response(self, instance):
        """
        格式化API响应数据
        """
        try:
            # 从输入框获取API响应数据
            raw_response = self.response_input.text

            # 尝试将数据解析为JSON对象
            parsed_response = json.loads(raw_response)

            # 将JSON对象格式化为字符串
            formatted_response = json.dumps(parsed_response, indent=4, ensure_ascii=False)

            # 将格式化后的数据显示在输出框中
            self.formatted_output.text = formatted_response
        except json.JSONDecodeError as e:
            # 处理JSON解析错误
            self.formatted_output.text = f'解析错误: {str(e)}'

if __name__ == '__main__':
    ApiResponseFormatterApp().run()