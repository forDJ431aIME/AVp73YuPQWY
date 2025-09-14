# 代码生成时间: 2025-09-14 17:31:04
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

class MessageNotificationSystem(FloatLayout):
    """
    A Kivy widget for displaying message notifications.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._notifications = []
        self._notification_timer = None

    def show_notification(self, message, timeout=3):
        """
        Show a notification message for a specified timeout.
        :param message: The message to display in the notification.
        :param timeout: The duration in seconds to display the notification.
        """
        # Create a new Label for the notification message
        notification_label = Label(text=message, size_hint=(None, None), size=(200, 50))

        # Add the label to the layout
        self.add_widget(notification_label)
        notification_label.pos_hint = {'x': 0.5, 'y': 0.9}
        notification_label.text_size = (200, 50)
        notification_label.valign = 'middle'
        notification_label.halign = 'center'

        # Schedule the removal of the notification after the specified timeout
        self._schedule_notification_removal(notification_label, timeout)

    def _schedule_notification_removal(self, notification_label, timeout):
        """
        Schedule the removal of a notification after a specified timeout.
        :param notification_label: The Label to be removed.
        :param timeout: The duration in seconds before removal.
        """
        # Cancel any existing timer
        if self._notification_timer:
            Clock.unschedule(self._notification_timer)

        # Schedule the removal of the notification
        self._notification_timer = Clock.schedule_once(self._remove_notification, timeout, notification_label)

    def _remove_notification(self, dt, notification_label):
        """
        Remove a notification label from the layout.
        :param dt: The time delta (unused).
        :param notification_label: The Label to be removed.
        """
        # Remove the notification label from the layout
        self.remove_widget(notification_label)
        self._notification_timer = None

    def on_touch_down(self, touch):
        """
        Override the touch_down event to dismiss notifications on touch.
        """
        if self.collide_point(*touch.pos):
            for widget in reversed(self.children):
                if isinstance(widget, Label):
                    self.remove_widget(widget)
        return super().on_touch_down(touch)

class MessageNotificationApp(App):
    """
    The main application class.
    """
    def build(self):
        self.root = MessageNotificationSystem()
        return self.root

    def on_start(self):
        """
        Display a notification on app start.
        """
        self.root.show_notification("Welcome to the message notification system!", 5)

if __name__ == '__main__':
    MessageNotificationApp().run()