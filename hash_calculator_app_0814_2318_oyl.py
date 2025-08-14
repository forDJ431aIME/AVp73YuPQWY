# 代码生成时间: 2025-08-14 23:18:21
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kivy application for calculating hash values.
"""
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

class HashCalculatorApp(App):
    def build(self):
        # Layout for the application
        layout = BoxLayout(orientation='vertical')

        # Input field for the text to be hashed
        self.text_input = TextInput(text='', size_hint_y=None, height=50)
        layout.add_widget(self.text_input)

        # Button to calculate the hash
        calculate_button = Button(text='Calculate Hash')
        calculate_button.bind(on_press=self.calculate_hash)
        layout.add_widget(calculate_button)

        # Label to display the hash result
        self.result_label = Label(text='', size_hint_y=None, height=50)
        layout.add_widget(self.result_label)

        return layout

    def calculate_hash(self, instance):
        """Calculates the hash of the input text and displays it."""
        try:
            # Get the text from the input field
            input_text = self.text_input.text
            if input_text:
                # Calculate the hash (using SHA256 for this example)
                hash_object = hashlib.sha256(input_text.encode())
                hash_hex = hash_object.hexdigest()

                # Display the hash result
                self.result_label.text = 'Hash: {}'.format(hash_hex)
            else:
                # Display an error message if the input field is empty
                self.show_error_popup('Input field cannot be empty.')
        except Exception as e:
            # Handle any exceptions that occur during hashing
            self.show_error_popup(str(e))

    def show_error_popup(self, message):
        """Displays an error message in a popup."""
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

if __name__ == '__main__':
    HashCalculatorApp().run()