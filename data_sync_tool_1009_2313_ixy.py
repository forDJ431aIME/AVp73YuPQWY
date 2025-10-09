# 代码生成时间: 2025-10-09 23:13:48
import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView, FileChooserPopup
from kivy.logger import Logger

"""
数据同步工具主程序
""""

class DataSyncToolApp(App):
    def build(self):
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical')

        # 创建源目录选择器
        self.source_chooser = FileChooserListView()
        self.source_chooser.allow_filesystem = True
        self.source_chooser.filters = []
        self.source_chooser.path = os.path.expanduser('~')

        # 创建目标目录选择器
        self.target_chooser = FileChooserListView()
        self.target_chooser.allow_filesystem = True
        self.target_chooser.filters = []
        self.target_chooser.path = os.path.expanduser('~')

        # 绑定源目录选择器事件
        self.source_chooser.bind(on_enter=self.on_source_enter)

        # 绑定目标目录选择器事件
        self.target_chooser.bind(on_enter=self.on_target_enter)

        # 创建按钮
        sync_button = Button(text='同步', on_press=self.on_sync)

        # 创建标签
        self.status_label = Label(text='请选择源目录和目标目录')

        # 添加组件到布局
        main_layout.add_widget(self.source_chooser)
        main_layout.add_widget(self.target_chooser)
        main_layout.add_widget(sync_button)
        main_layout.add_widget(self.status_label)

        return main_layout

    def on_source_enter(self, instance, value):
        """
        源目录选择器事件处理函数
        """"
        if value:
            self.source_path = value[0]
            self.status_label.text = '源目录已选择: ' + self.source_path

    def on_target_enter(self, instance, value):
        """
        目标目录选择器事件处理函数
        """"
        if value:
            self.target_path = value[0]
            self.status_label.text = '目标目录已选择: ' + self.target_path

    def on_sync(self, instance):
        """
        同步按钮事件处理函数
        """"
        if not self.source_path or not self.target_path:
            self.status_label.text = '请选择源目录和目标目录'
            return

        try:
            # 同步源目录到目标目录
            shutil.copytree(self.source_path, self.target_path)
            self.status_label.text = '同步成功'
        except Exception as e:
            Logger.error(f'同步失败: {e}')
            self.status_label.text = '同步失败'

# 运行程序
if __name__ == '__main__':
    DataSyncToolApp().run()