# 代码生成时间: 2025-10-13 03:06:26
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.clock import Clock
import psutil
import threading

# Custom ListItemButton for Process List
class ProcessItem(ListItemButton):
    def __init__(self, **kwargs):
        super(ProcessItem, self).__init__(**kwargs)
        self.bind(on_press=self._on_press)

    def _on_press(self, instance):
        """Open a popup with the option to kill the process."""
        process_id = self.text.split(':')[0]
        popup = Factory.PopupContent(process_id)
        popup.open()

# Popup Content
class PopupContent(Popup):
    def __init__(self, process_id, **kwargs):
        super(PopupContent, self).__init__(**kwargs)
        self.process_id = process_id
        self.title = 'Process Options'
        self.add_widget(Factory.KillProcessButton)

# Factory for Kill Process Button
Factory.register('KillProcessButton', cls=Factory.Button)
class KillProcessButton(Factory.Button):
    def on_release(self):
        "