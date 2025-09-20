# 代码生成时间: 2025-09-21 05:09:56
import zipfile
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.spinner import Spinner

# Define the main interface
class UnzipToolApp(App):
    def build(self):
        return UnzipToolLayout()

# Define the main layout
class UnzipToolLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(UnzipToolLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        # Add the file chooser for selecting the zip file
        self.zip_file_chooser = FileChooserListView()
        self.zip_file_chooser.dirselect = True
        self.zip_file_chooser.size_hint = (0.9, 0.3)
        self.zip_file_chooser.bind(on_submit=self.select_zip_file)
        self.add_widget(self.zip_file_chooser)

        # Add the spinner for selecting the destination folder
        self.destination_spinner = Spinner()
        self.destination_spinner.size_hint = (0.9, 0.3)
        self.destination_spinner.values = []
        self.add_widget(self.destination_spinner)

        # Add the button to start the unzip process
        self.unzip_button = Button(text='Unzip')
        self.unzip_button.size_hint = (0.9, 0.3)
        self.unzip_button.bind(on_release=self.unzip_file)
        self.add_widget(self.unzip_button)

        # Add a label to display the result
        self.result_label = Label(text='', size_hint=(0.9, 0.3))
        self.add_widget(self.result_label)

    def select_zip_file(self, instance, value):
        # Get the selected zip file path
        self.zip_file_path = value[0]
        # Update the destination folder spinner with available folders
        self.update_destination_folders()

    def update_destination_folders(self):
        # Get available folders in the system
        folders = [os.path.join(dp, d) for dp, dn, filenames in os.walk('/') for d in dn]
        self.destination_spinner.values = folders

    def unzip_file(self, instance):
        # Get the selected destination folder
        destination_folder = self.destination_spinner.values[0]
        # Try to unzip the file
        try:
            with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            self.result_label.text = 'File unzipped successfully!'
        except Exception as e:
            self.result_label.text = 'Error: ' + str(e)

# Define the Kivy application
if __name__ == '__main__':
    UnzipToolApp().run()