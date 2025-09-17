# 代码生成时间: 2025-09-17 08:41:00
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
import os

"""
Text File Analyzer using Kivy framework.

This application allows users to open a text file and analyze its content.
It provides basic statistics such as line count, word count, character count.
"""

class TextAnalyzerApp(App):
    def build(self):
        # Initialize the main layout
        self.main_layout = BoxLayout(orientation='vertical')
        return self.main_layout

    def open_file(self):
        """
        Opens a file dialog to select a text file and analyzes its content.
        """
        filechooser = FileChooserListView(
            dir=os.path.expanduser('~'),
            filters=['*.txt'],
            size_hint=(0.9, 0.9)
        )
        popup = Popup(title='Open File', content=filechooser, size_hint=(0.9, 0.9))
        popup.open()
        filechooser.bind(
            on_submit=self.file_selected
        )

    def file_selected(self, instance):
        """
        Handles the file selection and performs analysis on the selected file.
        """
        try:
            with open(instance.selection[0], 'r') as file:
                content = file.read()
                self.analyze_content(content)
        except Exception as e:
            self.show_error_popup(str(e))

    def analyze_content(self, content):
        """
        Analyzes the content of the text file.
        """
        line_count = content.count('
') + 1
        word_count = len(content.split())
        char_count = len(content)

        analysis_results = f"Line Count: {line_count}
Word Count: {word_count}
Character Count: {char_count}"

        # Display the analysis results
        label = Label(text=analysis_results)
        self.main_layout.add_widget(label)

    def show_error_popup(self, error_message):
        """
        Displays an error popup with the given error message.
        """
        popup = Popup(title='Error', content=Label(text=error_message), size_hint=(0.5, 0.5))
        popup.open()

    def build_config(self, config):
        """
        Configures the application settings.
        """
        Window.size = (800, 600)  # Set the default window size

if __name__ == '__main__':
    
    # Create an instance of the TextAnalyzerApp
    text_analyzer_app = TextAnalyzerApp()

    # Run the application
    text_analyzer_app.run()