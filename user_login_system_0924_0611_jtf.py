# 代码生成时间: 2025-09-24 06:11:00
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

"""
用户登录验证系统
"""
class LoginApp(App):
    def build(self):
        self.title = '用户登录验证系统'
        return self.login_ui()

    def login_ui(self):
        """
        构建登录界面
        """
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='用户名'))
        username_input = TextInput(multiline=False)
        layout.add_widget(username_input)
        layout.add_widget(Label(text='密码'))
        password_input = TextInput(password=True, multiline=False)
        layout.add_widget(password_input)

        login_button = Button(text='登录')
        login_button.bind(on_press=self.validate_login)
        layout.add_widget(login_button)

        return layout

    def validate_login(self, instance):
        """
        验证用户名和密码
        """
        root = self.root
        username = root.children[1].text
        password = root.children[3].text
        if username == 'admin' and password == 'password':
            popup = Popup(title='登录成功', content=Label(text='欢迎回来，管理员！'), size_hint=(None, None), size=(200, 200))
            popup.open()
        else:
            popup = Popup(title='登录失败', content=Label(text='用户名或密码错误'), size_hint=(None, None), size=(200, 200))
            popup.open()

# 运行程序
if __name__ == '__main__':
    kivy.require('2.0.0')
    LoginApp().run()