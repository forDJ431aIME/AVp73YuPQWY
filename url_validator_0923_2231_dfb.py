# 代码生成时间: 2025-09-23 22:31:43
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from urllib.parse import urlparse
import requests

"""
URL Validator using Python and Kivy framework.

This program creates a simple GUI application that allows users to enter a URL
and checks its validity by attempting to make an HTTP GET request to the URL.
"""

class UrlValidatorApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create the text input for the URL
        self.url_input = TextInput(multiline=False, hint_text='Enter URL here')
        main_layout.add_widget(self.url_input)

        # Create the check button
        check_button = Button(text='Check URL')
        check_button.bind(on_press=self.check_url)
        main_layout.add_widget(check_button)

        # Create the label to display the result
        self.result_label = Label(text='URL validity: Unknown')
        main_layout.add_widget(self.result_label)

        return main_layout

    def check_url(self, instance):
        # Get the URL from the input field
        url = self.url_input.text

        # Validate the URL using urlparse
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                self.result_label.text = 'Invalid URL'
                return

            # Attempt to make a GET request to the URL
            response = requests.get(url)
            if response.status_code == 200:
                self.result_label.text = 'Valid URL'
            else:
                self.result_label.text = 'URL not reachable'
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the GET request
            self.result_label.text = f'Error: {e}'
        except ValueError:
            # Handle invalid URL format
            self.result_label.text = 'Invalid URL format'

if __name__ == '__main__':
    UrlValidatorApp().run()
