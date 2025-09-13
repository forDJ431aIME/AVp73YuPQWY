# 代码生成时间: 2025-09-13 22:38:25
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

"""
HTTP请求处理器
使用KIVY框架创建一个简单的HTTP请求处理器应用
"""

class HttpRequestHandlerApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')

        # 创建标签显示HTTP请求状态
        self.status_label = Label(text='HTTP请求处理中...')
        layout.add_widget(self.status_label)

        # 创建请求URL输入框
        self.url_input = Label(text='请输入请求URL:')
        layout.add_widget(self.url_input)
        self.url_entry = Label(text='', halign='left')
        layout.add_widget(self.url_entry)

        # 创建发送按钮
        self.send_button = Button(text='发送HTTP请求')
        self.send_button.bind(on_press=self.send_http_request)
        layout.add_widget(self.send_button)

        # 创建响应显示区域
        self.response_label = Label(text='', size_hint_y=None)
        layout.add_widget(ScrollView(scroll_type='vertical', bar_width='10dp', size_hint=(1, 1), do_scroll_x=False))
        self.response_label.bind(size=self._update_scrollview_size)
        layout.add_widget(self.response_label)

        return layout

    def _update_scrollview_size(self, instance, value):
        instance.setter('height', value)

    def send_http_request(self, instance):
        try:
            # 获取输入的URL
            url = self.url_entry.text
            if not url:
                raise ValueError('URL不能为空')

            # 创建URL请求
            self.status_label.text = '发送HTTP请求...'
            request = UrlRequest(url, on_success=self.on_success, on_failure=self.on_failure, on_error=self.on_error, on_progress=self.on_progress)
            request.start()
        except Exception as e:
            # 显示错误信息
            self.status_label.text = f'HTTP请求错误: {e}'

    def on_success(self, request, result):
        # 请求成功，显示响应内容
        self.status_label.text = 'HTTP请求成功'
        self.response_label.text = result

    def on_failure(self, request, result):
        # 请求失败，显示失败信息
        self.status_label.text = 'HTTP请求失败'
        self.response_label.text = f'失败原因: {result}'

    def on_error(self, request, error):
        # 请求发生错误，显示错误信息
        self.status_label.text = 'HTTP请求错误'
        self.response_label.text = f'错误信息: {error}'

    def on_progress(self, request, current, total):
        # 请求进度更新，显示进度信息
        self.status_label.text = f'发送HTTP请求... ({current}/{total})'

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 32:  # 空格键
            self.send_button.state = 'down'
            self.send_http_request(self.send_button)
            return True
        return False

if __name__ == '__main__':
    # 创建并运行应用
    HttpRequestHandlerApp().run()
