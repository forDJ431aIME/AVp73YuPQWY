# 代码生成时间: 2025-08-23 08:51:17
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.graphics import Color, Ellipse
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget


class InteractiveChartWidget(Widget):
    """
    Widget that allows the user to create an interactive chart.
    """
    def __init__(self, **kwargs):
        super(InteractiveChartWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (800, 600)
        with self.canvas:
            Color(1, 1, 1)
            self.chart = Scatter(size_hint=(1, 1))
            self.chart.do_scale = False
            self.chart.do_translation = False
    
    def add_point(self, pos):
        """Add a point to the chart."""
        with self.chart.canvas:
            Ellipse(pos=pos, size=(10, 10))
    
    def on_touch_down(self, touch):
        """Handle touch down event."""
        if touch.x < self.width and touch.y < self.height:
            touch.ud['selected'] = super(InteractiveChartWidget, self).collide_point(touch.x, touch.y)
            return super(InteractiveChartWidget, self).on_touch_down(touch)
        return False
    
    def on_touch_move(self, touch):
        """Handle touch move event."""
        if 'selected' in touch.ud:
            return super(InteractiveChartWidget, self).on_touch_move(touch)
        return False
    
    def on_touch_up(self, touch):
        """Handle touch up event."""
        if 'selected' in touch.ud:
            self.add_point((touch.x, touch.y))
            return super(InteractiveChartWidget, self).on_touch_up(touch)
        return False


class ChartApp(App):
    """
    Main application class for interactive chart generator.
    """
    def build(self):
        """
        Build the main layout of the application.
        """
        self.layout = BoxLayout(orientation='vertical')
        self.chart_widget = InteractiveChartWidget()
        self.layout.add_widget(self.chart_widget)

        # Add button to clear the chart
        self.clear_button = Button(text='Clear Chart')
        self.clear_button.bind(on_press=self.clear_chart)
        self.layout.add_widget(self.clear_button)
        return self.layout
    
    def clear_chart(self, instance):
        """
        Clear the chart by removing all points.
        """
        self.chart_widget.canvas.clear()


if __name__ == '__main__':
    ChartApp().run()