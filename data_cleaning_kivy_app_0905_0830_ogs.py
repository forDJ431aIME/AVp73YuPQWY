# 代码生成时间: 2025-09-05 08:30:05
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserPopup
from kivy.core.window import Window
import pandas as pd
import os
import io

# 数据清洗函数
def clean_data(file_path):
    try:
        # 读取数据文件
        df = pd.read_csv(file_path)
        # 这里可以根据需要添加数据清洗和预处理的代码
        # 例如，删除缺失值、填充缺失值、数据类型转换等
        # 此处示例：删除包含缺失值的行
        df_cleaned = df.dropna()
        return df_cleaned
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None

# Kivy 应用
class DataCleaningApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text="Data Cleaning and Preprocessing Tool"))

        # 加载文件按钮
        self.load_button = Button(text="Load Data File")
        self.load_button.bind(on_press=self.load_file)
        self.layout.add_widget(self.load_button)

        # 显示文件路径的标签
        self.file_path_label = Label(text="No file loaded")
        self.layout.add_widget(self.file_path_label)

        # 数据清洗按钮
        self.clean_button = Button(text="Clean Data")
        self.clean_button.bind(on_press=self.clean_data)
        self.layout.add_widget(self.clean_button)

        # 显示清洗后数据的标签
        self.cleaned_data_label = Label(text="")
        self.layout.add_widget(self.cleaned_data_label)

        return self.layout

    def load_file(self, instance):
        # 打开文件选择器
        content = FileChooserPopup(select=self.select_file)
        content.open()

    def select_file(self, selection):
        # 设置文件路径标签
        if selection:
            self.file_path_label.text = selection[0]
            self.file_path = selection[0]

    def clean_data(self, instance):
        # 读取并清洗数据
        df_cleaned = clean_data(self.file_path)
        if df_cleaned is not None:
            # 将清洗后的数据转换为字符串显示
            cleaned_data_str = df_cleaned.to_csv(index=False)
            self.cleaned_data_label.text = cleaned_data_str
        else:
            self.cleaned_data_label.text = "Data cleaning failed"

# 运行应用
if __name__ == '__main__':
    DataCleaningApp().run()