# 代码生成时间: 2025-08-03 13:54:32
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.clock import Clock
import psutil

"""
系统性能监控工具
使用Python和Kivy框架实现
"""

class SystemMonitorApp(App):
    def build(self):
        # 创建布局
        layout = BoxLayout(orientation='vertical')

        # 创建CPU使用率标签
        self.cpu_label = Label(text='CPU Usage: 0%')
        layout.add_widget(self.cpu_label)

        # 创建内存使用率标签
        self.mem_label = Label(text='Memory Usage: 0%')
        layout.add_widget(self.mem_label)

        # 创建更新频率滑块
        self.slider = Slider(min=1, max=10, value=5)
        self.slider.bind(value=self.update_frequency)
        layout.add_widget(self.slider)

        # 返回布局
        return layout

    def on_start(self):
        # 启动时开始更新性能数据
        self.update_performance()

    def update_frequency(self, instance, value):
        # 更新更新频率
        self.stop_performance()
        self.start_performance(value)

    def start_performance(self, frequency):
        # 开始更新性能数据
        Clock.schedule_interval(self.update_performance, frequency)

    def stop_performance(self):
        # 停止更新性能数据
        Clock.unschedule(self.update_performance)

    def update_performance(self, dt):
        # 更新性能数据
        try:
            cpu_usage = psutil.cpu_percent()
            mem_usage = psutil.virtual_memory().percent
        
            # 更新CPU使用率标签
            self.cpu_label.text = f'CPU Usage: {cpu_usage}%'
        
            # 更新内存使用率标签
            self.mem_label.text = f'Memory Usage: {mem_usage}%'
        except Exception as e:
            # 错误处理
            print(f'Error updating performance data: {e}')

if __name__ == '__main__':
    SystemMonitorApp().run()
