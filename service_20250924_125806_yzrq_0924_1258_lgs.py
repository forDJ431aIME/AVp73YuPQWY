# 代码生成时间: 2025-09-24 12:58:06
import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from kivy.core.window import Window

# 文件夹结构整理器应用类
class FolderStructureOrganizerApp(App):
    def __init__(self, **kwargs):
        super(FolderStructureOrganizerApp, self).__init__(**kwargs)
        self.source_directory = ''
        self.target_directory = ''
        self.organize_button_disabled = True

    def select_source_directory(self):
        # 选择源文件夹
        popup = FileChooserPopup(select=self.source_directory_selected)
        popup.open()

    def source_directory_selected(self, selection, selection_dir):
        # 处理选择源文件夹
        if selection:
            self.source_directory = selection[0]
            self.root.ids.source_path.text = self.source_directory
            self.check_organize_button_state()

    def select_target_directory(self):
        # 选择目标文件夹
        popup = FileChooserPopup(select=self.target_directory_selected)
        popup.open()

    def target_directory_selected(self, selection, selection_dir):
        # 处理选择目标文件夹
        if selection:
            self.target_directory = selection[0]
            self.root.ids.target_path.text = self.target_directory
            self.check_organize_button_state()

    def check_organize_button_state(self):
        # 检查组织按钮状态
        self.root.ids.organize_button.disabled = not (self.source_directory and self.target_directory)

    def organize_folder_structure(self):
        # 组织文件夹结构
        try:
            self.organize_folders(self.source_directory, self.target_directory)
            self.root.ids.status_label.text = 'Folder structure organized successfully!'
        except Exception as e:
            self.root.ids.status_label.text = f'Error: {e}'

    def organize_folders(self, source, target):
        # 递归组织文件夹
        for item in os.listdir(source):
            source_item_path = os.path.join(source, item)
            target_item_path = os.path.join(target, item)
            if os.path.isdir(source_item_path):
                if not os.path.exists(target_item_path):
                    os.makedirs(target_item_path)
                self.organize_folders(source_item_path, target_item_path)
            else:
                shutil.copy2(source_item_path, target_item_path)

    def build(self):
        # 构建界面
        self.root = FolderStructureOrganizerLayout()
        return self.root

# 文件夹结构整理器布局类
class FolderStructureOrganizerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FolderStructureOrganizerLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.source_path_label = Label(text='Source Path: ')
        self.source_path = TextInput(multiline=False)
        self.source_path_button = Button(text='Browse', on_press=self.select_source_directory)
        self.source_path_layout = BoxLayout(size_hint_y=None, height=40)
        self.source_path_layout.add_widget(self.source_path_label)
        self.source_path_layout.add_widget(self.source_path)
        self.source_path_layout.add_widget(self.source_path_button)

        self.target_path_label = Label(text='Target Path: ')
        self.target_path = TextInput(multiline=False)
        self.target_path_button = Button(text='Browse', on_press=self.select_target_directory)
        self.target_path_layout = BoxLayout(size_hint_y=None, height=40)
        self.target_path_layout.add_widget(self.target_path_label)
        self.target_path_layout.add_widget(self.target_path)
        self.target_path_layout.add_widget(self.target_path_button)

        self.organize_button = Button(text='Organize', disabled=True, on_press=self.organize_folder_structure)
        self.status_label = Label(text='')

        self.add_widget(self.source_path_layout)
        self.add_widget(self.target_path_layout)
        self.add_widget(self.organize_button)
        self.add_widget(self.status_label)

# 初始化Kivy应用
if __name__ == '__main__':
    FolderStructureOrganizerApp().run()
