# 代码生成时间: 2025-08-26 06:45:42
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random
import datetime

# 消息通知系统App类
class MessageNotificationSystemApp(App):
    def build(self):
        # 创建主布局
        self.main_layout = BoxLayout(orientation='vertical')
        
        # 创建显示消息的标签
        self.message_label = Label(text='No messages', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.message_label)
        
        # 创建发送消息按钮
        self.send_message_button = Button(text='Send Message', size_hint_y=None, height=50)
        self.send_message_button.bind(on_press=self.send_message)
        self.main_layout.add_widget(self.send_message_button)
        
        # 返回主布局
        return self.main_layout
        
    def send_message(self, instance):
        # 生成随机消息
        message = f'Message at {datetime.datetime.now()}'
        
        # 显示消息
        self.show_message(message)
        
    def show_message(self, message):
        # 更新消息标签
        self.message_label.text = message
        
        # 显示一个弹出窗口以通知消息
        popup = Popup(title='New Message', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()
        
        # 5秒后自动关闭弹出窗口
        Clock.schedule_once(lambda dt: popup.dismiss(), 5)
        
# 如果直接运行此文件，则启动App
if __name__ == '__main__':
    MessageNotificationSystemApp().run()