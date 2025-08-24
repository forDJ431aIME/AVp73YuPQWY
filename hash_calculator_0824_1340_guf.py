# 代码生成时间: 2025-08-24 13:40:18
# hash_calculator.py
# A simple hash calculator tool using Python and Kivy framework.

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import hashlib
import os

class HashCalculatorApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create a text input for user to enter data
        self.data_input = TextInput(multiline=False)
        main_layout.add_widget(self.data_input)

        # Create a button to calculate hash
        calculate_button = Button(text='Calculate Hash')
        calculate_button.bind(on_press=self.calculate_hash)
        main_layout.add_widget(calculate_button)

        # Create a label to display the hash result
        self.hash_result = Label(text='')
        main_layout.add_widget(self.hash_result)

        return main_layout

    def calculate_hash(self, instance):
        # Get the data from the text input
        data = self.data_input.text

        # Check if the input is not empty
        if not data:
            self.show_error_popup('Please enter some data to calculate the hash.')
            return

        # Calculate the hash using SHA256
        try:
            hash_object = hashlib.sha256(data.encode())
            hash_result = hash_object.hexdigest()
            self.hash_result.text = f'SHA256 Hash: {hash_result}'
        except Exception as e:
            self.show_error_popup(f'An error occurred: {e}')

    def show_error_popup(self, message):
        # Create a popup to display error messages
        error_popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 100))
        error_popup.open()

# Check if this is the main module and run the app
if __name__ == '__main__':
    HashCalculatorApp().run()
