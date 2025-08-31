# 代码生成时间: 2025-09-01 06:25:55
import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileChooserPopup

"""
文件备份和同步工具
使用KIVY框架创建一个简单的图形用户界面(GUI)
实现文件备份和同步功能
"""

class FileBackupSyncApp(App):
    def build(self):
        # 创建一个垂直布局
        layout = BoxLayout(orientation='vertical')

        # 创建源文件选择器
        self.source_file_chooser = FileChooserListView()
        self.source_file_chooser.size_hint = (0.4, 0.3)
        self.source_file_chooser.filters = ['*.*']
        layout.add_widget(self.source_file_chooser)

        # 创建目标文件选择器
        self.target_file_chooser = FileChooserListView()
        self.target_file_chooser.size_hint = (0.4, 0.3)
        self.target_file_chooser.filters = ['*.*']
        layout.add_widget(self.target_file_chooser)

        # 创建备份按钮
        backup_button = Button(text='备份文件')
        backup_button.bind(on_press=self.backup_files)
        layout.add_widget(backup_button)

        # 创建同步按钮
        sync_button = Button(text='同步文件')
        sync_button.bind(on_press=self.sync_files)
        layout.add_widget(sync_button)

        return layout

    def backup_files(self, instance):
        """
        备份文件到目标目录
        """
        source_dir = self.source_file_chooser.path
        target_dir = self.target_file_chooser.path

        if not source_dir or not target_dir:
            self.root.ids['status_label'].text = '请选择源目录和目标目录'
            return

        try:
            # 遍历源目录
            for filename in os.listdir(source_dir):
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)

                # 如果源文件是目录，则递归备份
                if os.path.isdir(source_file):
                    shutil.copytree(source_file, target_file)
                # 如果源文件是文件，则复制文件
                else:
                    shutil.copy2(source_file, target_file)

            self.root.ids['status_label'].text = '文件备份成功'
        except Exception as e:
            self.root.ids['status_label'].text = f'备份失败: {str(e)}'

    def sync_files(self, instance):
        """
        同步文件到目标目录
        """
        source_dir = self.source_file_chooser.path
        target_dir = self.target_file_chooser.path

        if not source_dir or not target_dir:
            self.root.ids['status_label'].text = '请选择源目录和目标目录'
            return

        try:
            # 遍历源目录
            for filename in os.listdir(source_dir):
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)

                # 如果源文件是目录，则递归同步
                if os.path.isdir(source_file):
                    self.sync_files(instance)
                # 如果源文件是文件，则更新文件
                elif os.path.exists(target_file):
                    shutil.copy2(source_file, target_file)
                # 如果目标文件不存在，则复制文件
                else:
                    shutil.copy2(source_file, target_dir)

            self.root.ids['status_label'].text = '文件同步成功'
        except Exception as e:
            self.root.ids['status_label'].text = f'同步失败: {str(e)}'

# 运行程序
if __name__ == '__main__':
    FileBackupSyncApp().run()