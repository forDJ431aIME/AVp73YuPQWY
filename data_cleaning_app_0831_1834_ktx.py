# 代码生成时间: 2025-08-31 18:34:24
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np

# 数据清洗和预处理工具类
class DataCleaningApp(App):
    def build(self):
        # 设置主界面布局
        self.layout = BoxLayout(orientation='vertical')
        # 文件选择器
        self.file_choose = FileChooserIconView(size_hint=(1, 0.2))
        self.layout.add_widget(self.file_choose)
        # 加载文件按钮
        self.load_button = Button(text='Load File')
        self.load_button.bind(on_press=self.load_file)
        self.layout.add_widget(self.load_button)
        # 数据预览框
        self.preview_label = Label(text='Select a file to preview data')
        self.layout.add_widget(self.preview_label)
        # 清洗选项下拉菜单
        self.dropdown = DropDown()
        self.dropdown.add_widget(Label(text='Data Cleaning'))
        self.dropdown.add_widget(Button(text='Remove Duplicates', on_press=self.remove_duplicates))
        self.dropdown.add_widget(Button(text='Handle Missing Values', on_press=self.handle_missing_values))
        self.dropdown.add_widget(Button(text='Normalize Data', on_press=self.normalize_data))
        self.layout.add_widget(self.dropdown)
        # 清洗数据按钮
        self.clean_button = Button(text='Clean Data')
        self.clean_button.bind(on_press=self.clean_data)
        self.layout.add_widget(self.clean_button)
        # 保存文件按钮
        self.save_button = Button(text='Save Cleaned Data')
        self.save_button.bind(on_press=self.save_file)
        self.layout.add_widget(self.save_button)
        return self.layout
    
    def load_file(self, instance):
        # 加载文件
        self.file_choose.directory = ''
        self.file_choose.filters = ['*.csv']
        selected_path = self.file_choose.selection
        if len(selected_path) > 0:
            self.data = pd.read_csv(selected_path[0])
            self.preview_label.text = 'Data loaded successfully'
        else:
            self.preview_label.text = 'No file selected'
    
    def remove_duplicates(self, instance):
        # 移除重复数据
        if hasattr(self, 'data'):
            self.data = self.data.drop_duplicates()
            self.preview_label.text = 'Duplicates removed'
        else:
            self.preview_label.text = 'Load data first'
    
    def handle_missing_values(self, instance):
        # 处理缺失值
        if hasattr(self, 'data'):
            imputer = SimpleImputer(strategy='mean')
            self.data = pd.DataFrame(imputer.fit_transform(self.data), columns=self.data.columns)
            self.preview_label.text = 'Missing values handled'
        else:
            self.preview_label.text = 'Load data first'
    
    def normalize_data(self, instance):
        # 归一化数据
        if hasattr(self, 'data'):
            self.data = (self.data - self.data.mean()) / self.data.std()
            self.preview_label.text = 'Data normalized'
        else:
            self.preview_label.text = 'Load data first'
    
    def clean_data(self, instance):
        # 执行数据清洗
        self.remove_duplicates(None)
        self.handle_missing_values(None)
        self.normalize_data(None)
        self.preview_label.text = 'Data cleaned successfully'
    
    def save_file(self, instance):
        # 保存清洗后的数据
        if hasattr(self, 'data'):
            from kivy.utils import platform
            if platform == 'android':
                # Android平台保存文件
                self.data.to_csv('cleaned_data.csv', index=False)
                self.preview_label.text = 'Cleaned data saved'
            else:
                # 其他平台保存文件
                self.file_choose.directory = ''
                self.file_choose.filters = ['*.csv']
                self.file_choose.mode = 'save'
                file_path = self.file_choose.path
                if file_path:
                    self.data.to_csv(file_path, index=False)
                    self.preview_label.text = 'Cleaned data saved'
                else:
                    self.preview_label.text = 'No file path selected'
        else:
            self.preview_label.text = 'Load data first'

# 运行应用
if __name__ == '__main__':
    DataCleaningApp().run()