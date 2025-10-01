# 代码生成时间: 2025-10-02 02:20:28
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.clock import Clock
import hashlib
import logging

# 单点登录系统应用类
class SSOApp(App):
    def __init__(self, **kwargs):
        super(SSOApp, self).__init__(**kwargs)
        self.user = {}
        self.welcome_text = StringProperty('')
        self.start_time = 0

    # 处理用户登录
def build(self):
    root = BoxLayout(orientation='vertical')

    # 用户名输入框
    username_input = TextInput(multiline=False)
    username_input.bind(text=self.on_username_input)

    # 密码输入框
    password_input = TextInput(password=True, multiline=False)
    password_input.bind(text=self.on_password_input)

    # 登录按钮
    login_button = Button(text='Login')
    login_button.bind(on_press=self.login)

    # 登录成功或失败的提示文本
    welcome_label = Label(text=self.welcome_text)
    welcome_label.bind(texture_size=self.on_label_size)

    # 将组件添加到布局
    root.add_widget(username_input)
    root.add_widget(password_input)
    root.add_widget(login_button)
    root.add_widget(welcome_label)

    return root

    # 更新用户名输入框内容的事件处理
def on_username_input(self, instance, value):
    self.user['username'] = value

    # 更新密码输入框内容的事件处理
def on_password_input(self, instance, value):
    self.user['password'] = value

    # 登录事件处理
def login(self, instance):
    username = self.user.get('username')
    password = self.user.get('password')

    # 校验用户名和密码是否已输入
    if not username or not password:
        self.welcome_text = 'Please enter both username and password'
        return

    # 校验用户名和密码格式是否正确
    if len(username) < 4 or len(password) < 6:
        self.welcome_text = 'Username must be at least 4 characters and password must be at least 6 characters'
        return

    # 校验密码是否加密
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password != password:
        self.welcome_text = 'Password must be hashed'
        return

    # 登录成功
    self.welcome_text = f'Welcome {username}!'

    # 登录失败
    # 这里应当包含更多的错误处理逻辑，例如：
    # - 用户名不存在
    # - 用户名或密码错误
    # - 账户被锁定

    # 记录登录事件
    logging.info(f'User {username} logged in')

    # 记录登录时间
    Clock.schedule_once(lambda dt: setattr(self, 'start_time', time.time()), 0)

    # 调整标签大小以适应文本
def on_label_size(self, instance, value):
    instance.size_hint = (1, None)
    instance.height = instance.texture_size[1] + 10

    # 主函数入口
def main():
    SSOApp().run()

if __name__ == '__main__':
    main()
