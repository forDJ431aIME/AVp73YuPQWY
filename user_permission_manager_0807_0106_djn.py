# 代码生成时间: 2025-08-07 01:06:09
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, BooleanProperty
from kivy.lang import Builder
import json

Builder.load_string("""
<Root>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Add New User'
            on_press: app.add_new_user()
        Button:
            text: 'Delete User'
            on_press: app.delete_user()
        Button:
            text: 'Update User Permissions'
            on_press: app.update_user_permissions()
        Label:
            text: 'User List:'
        BoxLayout:
            id: user_list_box
""")

class UserPermissionManagerApp(App):
    user_list = ListProperty([])
    selected_user = BooleanProperty(False)
    new_user_name = ''
    new_user_permissions = []

    def build(self):
        self.root = Builder.load_file('user_permission_manager.kv')
        return self.root

    def load_user_data(self):
        """Load user data from a JSON file."""
        try:
            with open('users.json', 'r') as file:
                self.user_list = json.load(file)
        except FileNotFoundError:
            self.user_list = []
        except json.JSONDecodeError:
            self.show_error_popup('Invalid JSON format')

    def save_user_data(self):
        """Save user data to a JSON file."""
        try:
            with open('users.json', 'w') as file:
                json.dump(self.user_list, file)
        except Exception as e:
            self.show_error_popup(f'Error saving data: {e}')

    def add_new_user(self):
        """Add a new user with permissions."""
        popup = Popup(title='Add New User', content=self.create_user_popup_content())
        popup.open()

    def create_user_popup_content(self):
        """Create the content for the user popup."""
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='User Name:'))
        user_name_input = TextInput(text=self.new_user_name)
        user_name_input.bind(text=self.set_new_user_name)
        content.add_widget(user_name_input)
        content.add_widget(Label(text='Permissions (comma-separated):'))
        permissions_input = TextInput(text=','.join(self.new_user_permissions))
        permissions_input.bind(text=self.set_new_user_permissions)
        content.add_widget(permissions_input)
        add_button = Button(text='Add User')
        add_button.bind(on_press=self.add_user)
        content.add_widget(add_button)
        return content

    def set_new_user_name(self, instance, value):
        """Set the new user's name."""
        self.new_user_name = value

    def set_new_user_permissions(self, instance, value):
        "