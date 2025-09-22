# 代码生成时间: 2025-09-22 15:22:31
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
import math

"""
A simple math tools application using Kivy framework.
"""

class MathToolsApp(App):
    def build(self):
        # Initialize the screens
        self.screen_manager = ScreenManager()
        self.add_widget(self.screen_manager)
        
        # Add screens for different math operations
        self.add_math_screens()
        return self.screen_manager
    
    def add_math_screens(self):
        # Screen for basic arithmetic operations
        basic_arithmetic_screen = Screen(name='BasicArithmetic')
        basic_arithmetic_layout = GridLayout(rows=4, cols=2)
        basic_arithmetic_screen.add_widget(basic_arithmetic_layout)
        
        # Input fields for numbers
        num1_input = TextInput(text='', multiline=False)
        num2_input = TextInput(text='', multiline=False)
        basic_arithmetic_layout.add_widget(Label(text='Number 1:'))
        basic_arithmetic_layout.add_widget(num1_input)
        basic_arithmetic_layout.add_widget(Label(text='Number 2:'))
        basic_arithmetic_layout.add_widget(num2_input)
        
        # Buttons for basic arithmetic operations
        add_button = Button(text='+', size_hint=(0.4, 0.4))
        subtract_button = Button(text='-', size_hint=(0.4, 0.4))
        multiply_button = Button(text='*', size_hint=(0.4, 0.4))
        divide_button = Button(text='/', size_hint=(0.4, 0.4))
        
        # Add buttons to the layout
        basic_arithmetic_layout.add_widget(add_button)
        basic_arithmetic_layout.add_widget(subtract_button)
        basic_arithmetic_layout.add_widget(multiply_button)
        basic_arithmetic_layout.add_widget(divide_button)
        
        # Event handlers for buttons
        def add_handler(instance):
            num1 = float(num1_input.text)
            num2 = float(num2_input.text)
            result = num1 + num2
            self.show_result_popup('Result: ' + str(result))
        
        def subtract_handler(instance):
            num1 = float(num1_input.text)
            num2 = float(num2_input.text)
            result = num1 - num2
            self.show_result_popup('Result: ' + str(result))
        
        def multiply_handler(instance):
            num1 = float(num1_input.text)
            num2 = float(num2_input.text)
            result = num1 * num2
            self.show_result_popup('Result: ' + str(result))
        
        def divide_handler(instance):
            num1 = float(num1_input.text)
            num2 = float(num2_input.text)
            if num2 != 0:
                result = num1 / num2
                self.show_result_popup('Result: ' + str(result))
            else:
                self.show_result_popup('Error: Division by zero')
        
        # Bind button events
        add_button.bind(on_press=add_handler)
        subtract_button.bind(on_press=subtract_handler)
        multiply_button.bind(on_press=multiply_handler)
        divide_button.bind(on_press=divide_handler)
        
        # Add the screen to the screen manager
        self.screen_manager.add_widget(basic_arithmetic_screen)
        
    def show_result_popup(self, result_text):
        # Create a popup to display the result
        popup = Popup(title='Result', content=Label(text=result_text), size_hint=(None, None), size=(200, 200))
        popup.open()

if __name__ == '__main__':
    MathToolsApp().run()