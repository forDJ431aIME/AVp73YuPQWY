# 代码生成时间: 2025-09-08 10:30:21
# 引入kivy框架和sqlite3库
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import sqlite3


# 定义一个应用类
class AntiSQLInjectionApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')
        # 创建输入框
        self.username_input = TextInput(hint_text='Username', multiline=False)
        layout.add_widget(self.username_input)
        # 创建密码输入框
        self.password_input = TextInput(password=True, hint_text='Password', multiline=False)
        layout.add_widget(self.password_input)
        # 创建登录按钮
        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        # 返回主布局
        return layout

    def login(self, instance):
        # 获取输入的用户名和密码
        username = self.username_input.text
        password = self.password_input.text
        try:
            # 连接到数据库
            conn = sqlite3.connect('database.db')
            # 创建游标对象
            cursor = conn.cursor()
            # 使用参数化查询防止SQL注入
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            # 获取查询结果
            result = cursor.fetchone()
            # 关闭数据库连接
            conn.close()
            # 如果查询到用户则显示成功信息
            if result:
                self.show_popup('Login Success')
            else:
                self.show_popup('Login Failed')
        except sqlite3.Error as e:
            # 显示错误信息
            self.show_popup('Database error: ' + str(e))

    def show_popup(self, message):
        # 创建弹出框
        popup = Popup(title='Message', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        # 显示弹出框
        popup.open()


# 如果脚本直接运行，则运行应用
if __name__ == '__main__':
    AntiSQLInjectionApp().run()