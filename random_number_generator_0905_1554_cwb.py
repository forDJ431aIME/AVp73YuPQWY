# 代码生成时间: 2025-09-05 15:54:10
# random_number_generator.py
# This program is a random number generator using Python and Kivy framework.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from random import randint

class RandomNumberGenerator(Widget):
    """A widget that generates a random number."""
    random_number = NumericProperty()

    def on_touch_down(self, touch):
        # When the widget is touched, generate a new random number
        if self.collide_point(*touch.pos):
            self.random_number = randint(0, 100)
            return True
    
class RandomNumberApp(App):
    """The main application class."""
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Create a label to display the random number
        self.random_number_label = Label(text='Random Number:', size_hint=(1, 0.2))
        layout.add_widget(self.random_number_label)
        
        # Create the random number generator widget
        self.random_number_widget = RandomNumberGenerator()
        self.random_number_widget.bind(random_number=self.update_random_number)
        layout.add_widget(self.random_number_widget)
        
        return layout
    
    def update_random_number(self, instance, value):
        # Update the label with the new random number
        self.random_number_label.text = f'Random Number: {value}'

if __name__ == '__main__':
    # Run the application
    RandomNumberApp().run()