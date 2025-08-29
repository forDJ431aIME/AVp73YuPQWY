# 代码生成时间: 2025-08-29 21:01:46
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import threading
import queue
import time


# 消息通知系统类
class MessageNotificationSystem(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message_queue = queue.Queue()  # 消息队列
        self.is_active = True  # 系统是否激活

        # 初始化UI组件
        self.init_ui()

    def init_ui(self):
        # 创建标签和按钮
        self.message_label = Label(text='No message', font_size=20)
        self.notify_button = Button(text='Notify', font_size=20)

        # 设置布局
        layout = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        layout.add_widget(self.message_label)
        layout.add_widget(self.notify_button)

        # 添加按钮事件处理
        self.notify_button.bind(on_press=self.notify_message)

        # 将布局添加到Widget
        self.add_widget(layout)

    def notify_message(self, instance):
        # 从队列中获取消息
        try:
            message = self.message_queue.get_nowait()
        except queue.Empty:  # 队列为空时的处理
            self.message_label.text = 'No message'
            return

        # 显示消息
        self.message_label.text = message

    def add_message(self, message):
        # 将消息添加到队列
        self.message_queue.put(message)

    def start(self):
        # 启动消息处理线程
        self.is_active = True
        threading.Thread(target=self.process_messages).start()

    def stop(self):
        # 停止消息处理线程
        self.is_active = False

    def process_messages(self):
        # 消息处理循环
        while self.is_active:  # 检查系统是否激活
            try:
                message = self.message_queue.get(timeout=1)  # 从队列中获取消息，超时1秒

                # 显示消息
                self.message_label.text = message

                # 模拟消息处理时间
                time.sleep(2)

            except queue.Empty:  # 队列为空时的处理
                continue


# Kivy应用类
class MessageNotificationApp(App):
    def build(self):  # 构建应用
        # 创建消息通知系统实例
        self.notification_system = MessageNotificationSystem()

        # 启动消息处理线程
        self.notification_system.start()

        return self.notification_system

    def on_pause(self):  # 应用暂停时的处理
        # 停止消息处理线程
        self.notification_system.stop()

    def on_resume(self):  # 应用恢复时的处理
        # 重新启动消息处理线程
        self.notification_system.start()


# 程序入口
if __name__ == '__main__':
    # 创建消息并添加到队列
    message = 'Hello, this is a test message!'
    Window.bind(on_keyboard=MessageNotificationApp.instance.add_message)  # 绑定键盘事件，按下任意键时添加消息

    # 运行应用
    MessageNotificationApp().run()