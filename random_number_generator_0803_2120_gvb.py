# 代码生成时间: 2025-08-03 21:20:01
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from random import randint

class RandomNumberApp(App):
    def build(self):
        # Layout container
        layout = BoxLayout(orientation='vertical', padding=20)

        # Input for the user to enter the range of numbers
        self.lower_label = Label(text='Lower Bound:', size_hint_y=None, height=30)
        self.lower_input = TextInput(size_hint_y=None, height=30)
        self.upper_label = Label(text='Upper Bound:', size_hint_y=None, height=30)
        self.upper_input = TextInput(size_hint_y=None, height=30)

        # Button to generate a random number
        self.generate_button = Button(text='Generate', size_hint_y=None, height=40)
        self.generate_button.bind(on_press=self.generate_random)

        # Label to display the generated random number
        self.result_label = Label(text='Random Number:', size_hint_y=None, height=40)
        self.result_number = Label(size_hint_y=None, height=40)

        # Add widgets to the layout
        layout.add_widget(self.lower_label)
        layout.add_widget(self.lower_input)
        layout.add_widget(self.upper_label)
        layout.add_widget(self.upper_input)
        layout.add_widget(self.generate_button)
        layout.add_widget(self.result_label)
        layout.add_widget(self.result_number)

        return layout

    def generate_random(self, instance):
        try:
            # Attempt to get the lower and upper bounds from user input
            lower_bound = int(self.lower_input.text)
            upper_bound = int(self.upper_input.text)

            # Validate the bounds
            if lower_bound >= upper_bound:
                raise ValueError('Lower bound must be less than upper bound.')

            # Generate and display the random number
            random_number = randint(lower_bound, upper_bound)
            self.result_number.text = str(random_number)

        except ValueError as e:
            # Handle any errors in the input or random number generation
            self.result_number.text = 'Error: ' + str(e)

if __name__ == '__main__':
    RandomNumberApp().run()