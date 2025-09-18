# 代码生成时间: 2025-09-18 18:56:52
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
import threading
import sqlite3
import os

"""
Access Control Application using Kivy Framework.
This application allows users to log in, and access is controlled based on user roles.
"""

# Constants
DB_FILE = 'access_control.db'
USERNAME_FIELD = 'username'
PASSWORD_FIELD = 'password'
ROLE_FIELD = 'role'

# Role definitions
ADMIN_ROLE = 'admin'
USER_ROLE = 'user'

class AccessControlApp(App):
    def build(self):
        # Layout for login page
        self.login_layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(multiline=False, hint_text='Username')
        self.password_input = TextInput(multiline=False, hint_text='Password', password=True)
        self.login_button = Button(text='Login', on_press=self.login)
        self.error_label = Label(text='')

        # Add widgets to layout
        self.login_layout.add_widget(self.username_input)
        self.login_layout.add_widget(self.password_input)
        self.login_layout.add_widget(self.login_button)
        self.login_layout.add_widget(self.error_label)

        return self.login_layout

    def create_db(self):
        """Create the SQLite database with necessary tables."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            );""")
        conn.commit()
        conn.close()

    def check_credentials(self, username, password):
        """Check if the credentials are valid and return the user role."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def login(self, instance):
        """Handle the login button press event."""
        username = self.username_input.text
        password = self.password_input.text

        # Check if both fields are filled
        if not username or not password:
            self.error_label.text = 'Both username and password are required.'
            return

        # Check credentials in a separate thread to avoid UI freeze
        threading.Thread(target=self.check_login, args=(username, password)).start()

    def check_login(self, username, password):
        """Check login credentials and update UI accordingly."""
        role = self.check_credentials(username, password)
        if role:
            if role == ADMIN_ROLE:
                self.go_to_admin_page()
            elif role == USER_ROLE:
                self.go_to_user_page()
        else:
            self.error_label.text = 'Invalid username or password.'

    def go_to_admin_page(self):
        """Transition to the admin page."""
        self.root.clear_widgets()
        self.admin_layout = BoxLayout(orientation='vertical')
        self.admin_label = Label(text='Admin Page')
        self.admin_layout.add_widget(self.admin_label)
        self.root.add_widget(self.admin_layout)

    def go_to_user_page(self):
        """Transition to the user page."""
        self.root.clear_widgets()
        self.user_layout = BoxLayout(orientation='vertical')
        self.user_label = Label(text='User Page')
        self.user_layout.add_widget(self.user_label)
        self.root.add_widget(self.user_layout)

    def on_start(self):
        """Create the database on app start if it doesn't exist."""
        if not os.path.exists(DB_FILE):
            self.create_db()

if __name__ == '__main__':
    AccessControlApp().run()