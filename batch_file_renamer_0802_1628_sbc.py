# 代码生成时间: 2025-08-02 16:28:45
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import re

"""
Batch File Renamer is a Kivy-based application for renaming multiple files in a directory.
"""

class FileRenames(BoxLayout):
    def __init__(self, **kwargs):
        super(FileRenames, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Select a directory:'))
        self.add_widget(self._create_directory_chooser())
        self.add_widget(Label(text='Enter rename pattern (e.g., {index}_{name}):'))
        self.pattern_input = TextInput(multiline=False)
        self.add_widget(self.pattern_input)
        self.add_widget(Button(text='Rename Files', on_press=self.rename_files))

    def _create_directory_chooser(self):
        # Create a file chooser for selecting the directory
        dir_chooser = FileChooserListView(
            dirselect=True,
            path=os.getcwd(),
            filters={'All Files': [f"*.*"]},
        )
        dir_chooser.bind(
            on_submit=self.on_directory_selected,
        )
        return dir_chooser

    def on_directory_selected(self, instance, value, selection):
        # Handle directory selection
        self.selected_dir = value
        print(f'Selected directory: {self.selected_dir}')

    def rename_files(self, instance):
        # Rename files in the selected directory
        rename_pattern = self.pattern_input.text
        if not self.selected_dir:
            popup = Popup(title='Error', content=Label(text='Please select a directory first.'))
            popup.open()
            return
        
        try:
            for i, filename in enumerate(os.listdir(self.selected_dir)):
                old_path = os.path.join(self.selected_dir, filename)
                new_filename = re.sub(r'\{index\}_', f'{i+1}_', rename_pattern)
                new_filename = re.sub(r'\{name\}', filename, new_filename)
                new_path = os.path.join(self.selected_dir, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed {old_path} to {new_path}')
        except Exception as e:
            popup = Popup(title='Error', content=Label(text=str(e)))
            popup.open()

class FileRenamerApp(App):
    def build(self):
        return FileRenames()

if __name__ == '__main__':
    FileRenamerApp().run()
