# 代码生成时间: 2025-08-19 00:25:29
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import sqlite3

# Builder.load_string() allows us to define the UI in a string
Builder.load_string("""
au\
<SecureSqlApp>:
    BoxLayout:
        orientation: 'vertical'\
        Label:
            text: 'Enter Username:'\
         TextInput:
             id: username_input\
            text: ''\
            multiline: False\
        Label:
            text: 'Enter Password:'\
         TextInput:
             id: password_input\
             text: ''\
             multiline: False\
        Button:
            text: 'Login'\
            on_press: root.login()\
""")

class SecureSqlApp(App):
    
    def build(self):
        # Initialize root widget
        self.root = BoxLayout()
        return self.root
    
    def login(self):
        # Retrieve user input
        username = self.root.ids['username_input'].text
        password = self.root.ids['password_input'].text
        
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('secure_db.db')
            cursor = conn.cursor()
            
            # Use parameterized queries to prevent SQL injection
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            
            # Fetch results
            results = cursor.fetchall()
            
            # Check if the user exists
            if results:
                print("Login successful!")
            else:
                print("Login failed.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection
            if conn:
                conn.close()

if __name__ == '__main__':
    SecureSqlApp().run()