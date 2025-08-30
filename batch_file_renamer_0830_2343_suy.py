# 代码生成时间: 2025-08-30 23:43:49
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.utils import platform
from kivy.logger import Logger
import re

class BatchFileRenamerApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.file_chooser = FileChooserPopup(select=self.select_folder)
        self.layout.add_widget(self.file_chooser)
        self.rename_button = Button(text='Rename Files')
        self.rename_button.bind(on_release=self.rename_files)
        self.layout.add_widget(self.rename_button)
        return self.layout

    def select_folder(self, selection, selection_dir):
        """
        Handle folder selection.
        """
        self.file_chooser.dismiss()
        folder_path = selection_dir[0]  # Assuming single folder selection
        if folder_path:
            self.folder_path = folder_path
            self.populate_file_list(folder_path)
        else:
            raise ValueError('No folder selected')

    def populate_file_list(self, folder_path):
        """
        Populate the file list in the UI.
        """
        self.file_list = []
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                self.file_list.append(filename)
        self.update_file_list_ui()

    def update_file_list_ui(self):
        """
        Update the UI to display the file list.
        """
        # This function should be implemented to display the file list
        # For simplicity, we'll just print the file names
        for filename in self.file_list:
            print(filename)

    def rename_files(self, instance):
        """
        Rename files in the selected folder.
        """
        if not self.folder_path:
            raise ValueError('No folder selected')
        try:
            for index, filename in enumerate(self.file_list):
                # Simple renaming logic: append index to filename
                new_name = f'{index}_{filename}'
                os.rename(os.path.join(self.folder_path, filename),
                          os.path.join(self.folder_path, new_name))
        except Exception as e:
            Logger.error(f'Error renaming files: {e}')
            raise

    def on_pause(self):
        """
        Pause the app.
        """
        return True

# Run the app
BatchFileRenamerApp().run()
