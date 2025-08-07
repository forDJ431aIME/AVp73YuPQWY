# 代码生成时间: 2025-08-07 21:07:53
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import pandas as pd
import numpy as np
from typing import List
"""
A Kivy application for data cleaning and preprocessing.
"""

class DataCleaningApp(App):
    def build(self):
        return DataCleaningScreenManager()

class DataCleaningScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(DataCleaningScreen(name='main'))

class DataCleaningScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        # Add a label for instructions
        self.layout.add_widget(Label(text='Data Cleaning and Preprocessing Tool'))

        # Add file chooser
        self.file_chooser = FileChooserListView(size_hint=(1, 0.5))
        self.layout.add_widget(self.file_chooser)

        # Add a button to load data
        self.load_data_button = Button(text='Load Data')
        self.load_data_button.bind(on_press=self.load_data)
        self.layout.add_widget(self.load_data_button)

        # Add a button to clean data
        self.clean_data_button = Button(text='Clean Data')
        self.clean_data_button.bind(on_press=self.clean_data)
        self.layout.add_widget(self.clean_data_button)

        # Add a scroll view for displaying the data
        self.data_display = ScrollView()
        self.layout.add_widget(self.data_display)

        # Add a text input for additional cleaning commands
        self.cleaning_commands_input = TextInput(multiline=True)
        self.layout.add_widget(self.cleaning_commands_input)

        # Initialize a label for the data preview
        self.data_preview_label = Label()
        self.data_display.add_widget(self.data_preview_label)

    def load_data(self, instance):
        """
        Load data from the selected file.
        """
        try:
            file_path = self.file_chooser.path
            if file_path:
                self.df = pd.read_csv(file_path)
                self.update_data_preview()
        except Exception as e:
            self.show_error_popup('Error loading data', str(e))

    def clean_data(self, instance):
        """
        Clean data based on user input and predefined cleaning rules.
        """
        clean_commands = self.cleaning_commands_input.text
        try:
            # Example of a cleaning command: replace missing values with the mean
            if 'mean' in clean_commands:
                self.df.fillna(self.df.mean(), inplace=True)

            # Update the data preview after cleaning
            self.update_data_preview()
        except Exception as e:
            self.show_error_popup('Error cleaning data', str(e))

    def update_data_preview(self):
        """
        Update the data preview label with the current data.
        """
        if self.df is not None:
            preview_text = self.df.head().to_string(index=False)
            self.data_preview_label.text = preview_text
        else:
            self.data_preview_label.text = 'No data loaded.'

    def show_error_popup(self, title: str, message: str):
        """
        Display an error popup with the given title and message.
        """
        content = Label(text=message)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    DataCleaningApp().run()