# 代码生成时间: 2025-08-27 18:56:00
# theme_switcher.py

# A simple Kivy app demonstrating theme switching functionality


# Import necessary modules from Kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config


class ThemeSwitcherApp(App):

    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Add a button to switch themes
        theme_switch_button = Button(text='Switch Theme')
        theme_switch_button.bind(on_press=self.switch_theme)

        # Add the button to the layout
        layout.add_widget(theme_switch_button)

        return layout

    def switch_theme(self, instance):
        # List available themes
        available_themes = ['Default', 'Dark', 'Light']

        # Check if the current theme is not already selected
        current_theme = Config.get('kivy', 'theme')
        if current_theme not in available_themes:
            current_theme = 'Default'

        # Create a popup to select a new theme
        popup = Popup(title='Select Theme', size_hint=(None, None), size=(200, 200))
        theme_list = []

        # Create a button for each theme
        for theme in available_themes:
            if theme == current_theme:
                theme_button = Button(text=f'{theme} (current)', disabled=True)
            else:
                theme_button = Button(text=theme)
                theme_button.bind(on_press=lambda btn, t=theme: self.apply_theme(t))
            theme_list.append(theme_button)

        # Layout to hold the theme buttons
        theme_layout = BoxLayout(orientation='vertical')
        for theme_button in theme_list:
            theme_layout.add_widget(theme_button)

        # Add the theme layout to the popup
        popup.content = theme_layout
        popup.open()

    def apply_theme(self, theme):
        # Apply the selected theme
        Config.set('kivy', 'theme', theme)
        # Close all windows and reopen them to apply the new theme
        for window in Window._windows:
            window.close()
        self.stop()
        self.run()

# Run the app
if __name__ == '__main__':
    ThemeSwitcherApp().run()
