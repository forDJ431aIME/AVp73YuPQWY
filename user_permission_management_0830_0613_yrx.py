# 代码生成时间: 2025-08-30 06:13:17
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
import sqlite3

# 用户权限管理系统
class UserPermissionManagementApp(App):
    users_and_roles = ListProperty([
        {"username": "admin", "role": "admin"},
        {"username": "user", "role": "user"},
    ])
    username_input = ObjectProperty(TextInput())
    password_input = ObjectProperty(TextInput())

    def build(self):
        # 初始化数据库连接
        self.init_db()

        # 创建主布局
        main_layout = BoxLayout(orientation='vertical')

        # 添加用户名输入框
        username_label = Label(text='Username:')
        username_label.size_hint = (0.2, 0.1)
        main_layout.add_widget(username_label)
        main_layout.add_widget(self.username_input)

        # 添加密码输入框
        password_label = Label(text='Password:')
        password_label.size_hint = (0.2, 0.1)
        main_layout.add_widget(password_label)
        main_layout.add_widget(self.password_input)

        # 添加登录按钮
        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        main_layout.add_widget(login_button)

        # 显示用户权限
        self.show_user_permissions()

        # 返回主布局
        return main_layout

    def init_db(self):
        # 初始化数据库连接
        self.conn = sqlite3.connect('user_permissions.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            role TEXT
        )''')
        self.conn.commit()

    def login(self, instance):
        # 获取用户名和密码
        username = self.username_input.text
        password = self.password_input.text

        # 检查用户名和密码是否正确
        try:
            self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user_info = self.cursor.fetchone()
            if user_info:
                # 用户验证成功
                if user_info[2] == 'admin':
                    self.show_admin_permissions()
                else:
                    self.show_user_permissions()
            else:
                # 用户验证失败
                popup_content = Label(text='Invalid username or password')
                popup = Popup(title='Error', content=popup_content, size_hint=(0.2, 0.2))
                popup.open()
        except sqlite3.Error as e:
            # 数据库错误处理
            print(f'Database error: {e}')

    def show_admin_permissions(self):
        # 显示管理员权限
        popup_content = Label(text='Admin permissions')
        popup = Popup(title='Admin', content=popup_content, size_hint=(0.2, 0.2))
        popup.open()

    def show_user_permissions(self):
        # 显示用户权限
        popup_content = Label(text='User permissions')
        popup = Popup(title='User', content=popup_content, size_hint=(0.2, 0.2))
        popup.open()

    def on_stop(self):
        # 关闭数据库连接
        self.conn.close()

# 运行程序
if __name__ == '__main__':
    UserPermissionManagementApp().run()