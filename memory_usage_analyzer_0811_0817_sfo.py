# 代码生成时间: 2025-08-11 08:17:46
import psutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

# Define a class to collect and display memory usage
class MemoryUsageWidget(BoxLayout):
    memory_usage = StringProperty("")

    def __init__(self, **kwargs):
        super(MemoryUsageWidget, self).__init__(**kwargs)
        self.refresh_memory_usage()

    def refresh_memory_usage(self):
        "