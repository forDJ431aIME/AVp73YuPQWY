# 代码生成时间: 2025-09-17 12:49:33
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import matplotlib.pyplot as plt
import numpy as np


class InteractiveChart(BoxLayout):
    """
    A class to create an interactive chart generator using Kivy framework.
    This class handles user input and generates charts based on the input.
    """
    def __init__(self, **kwargs):
        super(InteractiveChart, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Enter data points (comma-separated): "))
        self.data_input = TextInput(multiline=False)
        self.add_widget(self.data_input)
        self.add_widget(Button(text="Generate Chart", on_release=self.generate_chart))
        self.add_widget(Label(text="Chart Options"))
        self.add_widget(ToggleButton(text="Show Grid"))
        self.add_widget(Slider(min=1, max=100, value=50, step=1))
        self.add_widget(ToggleButton(text="Show Legend"))
        self.add_widget(Label(text=""))  # Placeholder for chart
        self.chart_placeholder = Label(text="Chart will be displayed here.")
        self.add_widget(self.chart_placeholder)

    def generate_chart(self, instance):
        """
        Generate a chart based on the data points entered by the user.
        """
        try:
            data_points = self.data_input.text.split(',')
            data_points = [float(point.strip()) for point in data_points]
            x = np.arange(len(data_points))
            y = np.array(data_points)

            # Create a line chart using matplotlib
            fig, ax = plt.subplots()
            ax.plot(x, y, label='Data Points')

            # Check if grid and legend options are selected
            grid_toggle = self.ids.grid_toggle.state == 'down'
            legend_toggle = self.ids.legend_toggle.state == 'down'

            if grid_toggle:
                ax.grid(True)
            if legend_toggle:
                ax.legend()

            plt.tight_layout()
            fig.canvas.draw()

            # Save the plot to a temporary buffer and update the chart placeholder
            from io import BytesIO
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img = plt.imread(buffer)
            self.chart_placeholder.texture = img.texture
        except ValueError as e:
            # Handle invalid input
            self.chart_placeholder.text = "Invalid input: " + str(e)
        except Exception as e:
            # Handle any other unexpected errors
            self.chart_placeholder.text = "An error occurred: " + str(e)


class ChartApp(App):
    """
    The main application class.
    """
    def build(self):
        return InteractiveChart()


if __name__ == '__main__':
    ChartApp().run()