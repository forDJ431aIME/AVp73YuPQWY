# 代码生成时间: 2025-08-24 21:24:51
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.core.window import Window

class MathCalculatorApp(App):
    """Kivy application class for the math calculator."""
    def build(self):
        # Set the window size
        Window.size = (400, 600)
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create the input fields for the user to enter numbers
        self.input1 = TextInput(text='', multiline=False, size_hint=(1, 0.1))
        self.input2 = TextInput(text='', multiline=False, size_hint=(1, 0.1))
        main_layout.add_widget(self.input1)
        main_layout.add_widget(self.input2)

        # Create the label to display the results
        self.result_label = Label(text='', size_hint=(1, 0.1))
        main_layout.add_widget(self.result_label)

        # Create buttons for the mathematical operations
        operation_buttons = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        for operation in ['+', '-', '*', '/']:
            button = Button(text=operation)
            button.bind(on_press=lambda instance, op=operation: self.perform_operation(op))
            operation_buttons.add_widget(button)
        main_layout.add_widget(operation_buttons)

        # Return the main layout as the root widget
        return main_layout

    def perform_operation(self, operation):
        """Perform the mathematical operation on the input values."""
        try:
            # Get the input values from the text inputs
            value1 = float(self.input1.text)
            value2 = float(self.input2.text)

            # Perform the operation based on the button pressed
            if operation == '+':
                result = value1 + value2
            elif operation == '-':
                result = value1 - value2
            elif operation == '*':
                result = value1 * value2
            elif operation == '/':
                # Check for division by zero
                if value2 == 0:
                    raise ValueError('Division by zero is not allowed.')
                result = value1 / value2

            # Update the result label with the result
            self.result_label.text = f"{value1} {operation} {value2} = {result}"
        except ValueError as e:
            # Handle any value errors such as conversion to float or division by zero
            self.result_label.text = f"Error: {e}"
        except Exception as e:
            # Handle any other exceptions
            self.result_label.text = f"An error occurred: {e}"

if __name__ == '__main__':
    MathCalculatorApp().run()