# 代码生成时间: 2025-09-19 00:27:21
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import re
"""
FormValidatorKivyApp: A Kivy application that includes a form with validation.
"""

Builder.load_string(""""
<CustomLabel>:
    size_hint_y: None
    height: 40

<Screen>:
    BoxLayout:
        orientation: 'vertical'
        CustomLabel:
            text: 'Username'
        UsernameInput:
            id: username_input
            multiline: False
            hint_text: 'Enter username'
        CustomLabel:
            text: 'Email'
        EmailInput:
            id: email_input
            multiline: False
            hint_text: 'Enter email'
        Button:
            text: 'Submit'
            on_press: root.validate_form()
""")

class CustomLabel(Label):
    pass

class FormValidatorScreen(Screen):
    def __init__(self, **kwargs):
        super(FormValidatorScreen, self).__init__(**kwargs)
        self.username_input = self.ids['username_input']
        self.email_input = self.ids['email_input']

    def validate_form(self):
        """
        Validates the form data.

        Checks if the username is at least 3 characters long and if the email is in a valid format.

        Returns:
            bool: True if validation is successful, False otherwise.
        """
        username = self.username_input.text
        email = self.email_input.text

        if len(username) < 3:
            error_message = 'Username must be at least 3 characters long.'
            self.show_error_message(error_message)
            return False

        if not self.validate_email(email):
            error_message = 'Email is not in a valid format.'
            self.show_error_message(error_message)
            return False

        return True

    def validate_email(self, email):
        """
        Validates an email address using a regular expression.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def show_error_message(self, message):
        """
        Displays an error message on the screen.

        Args:
            message (str): The message to display.
        """
        error_label = Label(text=message, size_hint_y=None, height=40)
        self.add_widget(error_label)

class FormValidatorApp(App):
    def build(self):
        sm = ScreenManager()
        screen = FormValidatorScreen(name='form')
        sm.add_widget(screen)
        return sm

if __name__ == '__main__':
    FormValidatorApp().run()
