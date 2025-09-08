# 代码生成时间: 2025-09-09 05:35:42
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Define the Calculator class
class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create input fields
        self.input_display = TextInput(multiline=False, readonly=True, font_size='24sp')
        self.add_widget(self.input_display)

        # Create buttons for digits and operations
        buttons = [
            Button(text=str(i), font_size='24sp') for i in range(10)
        ] + [
            Button(text='+', font_size='24sp'),
            Button(text='-', font_size='24sp'),
            Button(text='*', font_size='24sp'),
            Button(text='/', font_size='24sp'),
            Button(text='C', font_size='24sp'),  # Clear button
            Button(text='=', font_size='24sp'),  # Equals button
        ]

        for button in buttons:
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)

    # Handle button press events
    def on_button_press(self, instance):
        if instance.text == 'C':
            self.input_display.text = ''
        elif instance.text == '=':
            self.calculate_result()
        else:
            self.input_display.text += instance.text

    # Perform the calculation
    def calculate_result(self):
        try:
            expression = self.input_display.text
            result = eval(expression)
            self.input_display.text = str(result)
        except Exception as e:
            self.input_display.text = 'Error'
            print(f'An error occurred: {e}')

# Define the Kivy App
class MathCalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    MathCalculatorApp().run()