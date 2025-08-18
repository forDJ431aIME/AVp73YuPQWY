# 代码生成时间: 2025-08-19 06:07:57
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json

# 模拟的用户数据库
USER_DATABASE = {
    "admin": "admin123",
    "user": "user123"
}

class LoginScreen(BoxLayout):
    # 初始化界面布局
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        # 创建用户名和密码输入框
        self.username_input = TextInput(text='', hint_text='Username', multiline=False)
        self.password_input = TextInput(text='', hint_text='Password', multiline=False, password=True)
        # 创建登录按钮
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.handle_login)
        # 将组件添加到布局中
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

    # 处理登录按钮事件
    def handle_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # 检查用户名和密码是否匹配
        if self.validate_credentials(username, password):
            # 登录成功，关闭登录窗口
            self.clear_widgets()
            self.add_widget(Label(text='Login successful!'))
        else:
            # 登录失败，显示错误消息
            popup = Popup(title='Login Failed', content=Label(text='Invalid username or password'), size_hint=(None, None), size=(200, 200))
            popup.open()

    # 验证用户凭据
    def validate_credentials(self, username, password):
        # 查找用户名和密码
        if username in USER_DATABASE and USER_DATABASE[username] == password:
            return True
        return False

# 创建Kivy应用程序
class UserLoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    UserLoginApp().run()