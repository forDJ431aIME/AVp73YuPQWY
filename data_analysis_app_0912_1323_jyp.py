# 代码生成时间: 2025-09-12 13:23:55
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserPopup
from kivy.core.window import Window
import pandas as pd
import numpy as np
from kivy.clock import Clock

# 统计数据分析器应用
class DataAnalysisApp(App):
    
    def build(self):
        # 创建一个垂直布局
        self.layout = BoxLayout(orientation='vertical')
        
        # 创建标签
        self.label = Label(text='选择数据文件进行分析')
        
        # 创建文件选择按钮
        self.btn_open = Button(text='打开文件')
        self.btn_open.bind(on_press=self.open_file)
        
        # 创建文本输入框，用于显示文件路径
        self.file_path_input = TextInput(multiline=False, readonly=True)
        
        # 创建分析按钮
        self.btn_analyze = Button(text='数据分析', disabled=True)
        self.btn_analyze.bind(on_press=self.analyze_data)
        
        # 将组件添加到布局
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn_open)
        self.layout.add_widget(self.file_path_input)
        self.layout.add_widget(self.btn_analyze)
        
        return self.layout
    
    def open_file(self, instance):
        # 打开文件选择对话框
        popup = FileChooserPopup(select=self.select_file)
        popup.open()
    
    def select_file(self, selection):
        # 选择文件后更新文件路径输入框
        if selection:
            self.file_path_input.text = selection[0]
            self.btn_analyze.disabled = False
    
    def analyze_data(self, instance):
        # 尝试加载并分析数据
        try:
            df = pd.read_csv(self.file_path_input.text)
            # 进行基本的数据分析
            mean = df.mean()
            std = df.std()
            sum = df.sum()
            print('Mean:', mean)
            print('Std Dev:', std)
            print('Sum:', sum)
        except Exception as e:
            # 显示错误信息
            self.label.text = '数据分析失败: ' + str(e)
    
class FileChooserPopup(kivy.uix.popup.Popup):
    def __init__(self, select, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.content = BoxLayout(orientation='vertical')
        self.filechooser = kivy.uix.filechooser.FileChooserIconView(
            path='./',
            filters=['*.csv'],
            size_hint=(0.9, 0.9)
        )
        self.btn_select = Button(text='选择文件')
        self.btn_select.bind(on_press=self.select)
        self.content.add_widget(self.filechooser)
        self.content.add_widget(self.btn_select)
        self.select = select
        self.add_widget(self.content)
    
    def select(self, instance):
        selection = self.filechooser.selection
        if selection:
            self.select(selection)
            self.dismiss()
        else:
            self.select([])
    
if __name__ == '__main__':
    DataAnalysisApp().run()