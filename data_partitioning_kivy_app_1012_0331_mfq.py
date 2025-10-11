# 代码生成时间: 2025-10-12 03:31:26
# 数据分片和分区工具
# 数据分片和分区工具是一个Kivy应用，它允许用户通过图形界面进行数据分片和分区。

# 导入所需的库
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.popup import Popup
from kivy.logger import Logger
import pandas as pd
import numpy as np


class DataPartitioningLayout(BoxLayout):
    # 初始化方法
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # 添加标题
        self.add_widget(Label(text='数据分片和分区工具', font_size=24))
        
        # 添加文件选择按钮
        self.file_button = Button(text='选择数据文件')
        self.file_button.bind(on_release=self.open_file_dialog)
        self.add_widget(self.file_button)
        
        # 添加文件路径显示
        self.file_path_label = Label(text='未选择文件')
        self.add_widget(self.file_path_label)
        
        # 添加分片大小输入框
        self.chunk_size_input = TextInput(hint_text='输入分片大小', multiline=False)
        self.add_widget(self.chunk_size_input)
        
        # 添加分区大小输入框
        self.partition_size_input = TextInput(hint_text='输入分区大小', multiline=False)
        self.add_widget(self.partition_size_input)
        
        # 添加分区按钮
        self.partition_button = Button(text='分片和分区')
        self.partition_button.bind(on_release=self.partition_data)
        self.add_widget(self.partition_button)
        
        # 添加结果显示标签
        self.result_label = Label(text='结果：')
        self.add_widget(self.result_label)

    # 打开文件对话框方法
    def open_file_dialog(self, instance):
        filechooser = FileChooserPopup(select=self.load_file)
        filechooser.open()
    
    # 加载文件方法
    def load_file(self, selection, selection_type, option):
        if selection:
            self.file_path_label.text = selection[0]
            self.data_file_path = selection[0]
        else:
            self.file_path_label.text = '未选择文件'
            self.data_file_path = None
    
    # 分片和分区方法
    def partition_data(self, instance):
        try:
            chunk_size = int(self.chunk_size_input.text)
            partition_size = int(self.partition_size_input.text)
            if self.data_file_path:
                # 读取数据文件
                data = pd.read_csv(self.data_file_path)
                # 分片
                chunks = np.array_split(data, chunk_size)
                # 分区
                partitions = []
                for i, chunk in enumerate(chunks):
                    partitions.append(chunk[0:partition_size])
                # 显示结果
                self.result_label.text = f'分片和分区完成，共有{len(partitions)}个分区'
            else:
                raise FileNotFoundError('未选择数据文件')
        except ValueError:
            self.result_label.text = '分片大小和分区大小必须是整数'
        except FileNotFoundError as e:
            self.result_label.text = str(e)
        except Exception as e:
            self.result_label.text = str(e)

class DataPartitioningApp(App):
    # 初始化方法
    def build(self):
        return DataPartitioningLayout()

# 运行应用
if __name__ == '__main__':
    DataPartitioningApp().run()