# 代码生成时间: 2025-08-14 18:40:57
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserPopup

"""
File Structure Manager
This application is designed to organize files within a selected directory.
It allows users to choose a directory and then automatically
sorts files into specific subdirectories based on file extensions.
"""

class FileStructureManager(App):
    # Initialize the application with a layout
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display instructions
        self.label = Label(text="Select a directory to organize:")
        layout.add_widget(self.label)

        # Button to open the file chooser popup
        self.button = Button(text="Select Directory")
        self.button.bind(on_release=self.open_file_chooser)
        layout.add_widget(self.button)

        # File chooser popup
        self._file_chooser = None
        self.open_file_chooser()

        return layout

    # Function to open the file chooser popup
    def open_file_chooser(self, instance):
        self._file_chooser = FileChooserPopup(select=self._select_directory)
        self._file_chooser.open()

    # Function to handle the selected directory
    def _select_directory(self, selection):
        if selection:
            directory_path = selection[0]
            self.organize_files(directory_path)
        else:
            self.label.text = "No directory selected."

    # Function to organize files in the selected directory
    def organize_files(self, directory_path):
        try:
            # Create subdirectories for different file types
            for extension in [".jpg", ".png", ".txt", ".pdf", ".docx"]:
                os.makedirs(os.path.join(directory_path, extension[1:]), exist_ok=True)

            # Move files into their respective subdirectories
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    extension = os.path.splitext(filename)[1].lower()
                    if extension:
                        destination_path = os.path.join(directory_path, extension[1:], filename)
                        os.replace(file_path, destination_path)

            self.label.text = "Files organized successfully."
        except Exception as e:
            self.label.text = f"An error occurred: {e}"

if __name__ == '__main__':
    FileStructureManager().run()
