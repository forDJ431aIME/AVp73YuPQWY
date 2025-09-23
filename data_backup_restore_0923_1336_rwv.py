# 代码生成时间: 2025-09-23 13:36:15
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import platform
from zipfile import ZipFile
from os import path, listdir
from shutil import copy2, copytree, rmtree
from datetime import datetime

# DataBackupRestoreApp is the main application class
class DataBackupRestoreApp(App):
    def build(self):
        # Layout setup
        layout = BoxLayout(orientation='vertical')

        # Add buttons for backup and restore
        self.backup_button = Button(text='Backup Data')
        self.restore_button = Button(text='Restore Data')
        self.backup_button.bind(on_press=self.backup_data)
        self.restore_button.bind(on_press=self.restore_data)

        # Add labels to show messages
        self.backup_label = Label(text='')
        self.restore_label = Label(text='')

        # Add widgets to the layout
        layout.add_widget(self.backup_button)
        layout.add_widget(self.backup_label)
        layout.add_widget(self.restore_button)
        layout.add_widget(self.restore_label)

        return layout

    def backup_data(self, instance):
        # Create backup directory and prepare the backup
        backup_dir = 'backup_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        data_dir = 'data'
        backup_path = path.join(data_dir, backup_dir)

        try:
            if not path.exists(data_dir):
                raise FileNotFoundError('Data directory not found.')
                
            # Copy the data directory to the backup directory
            copytree(data_dir, backup_path)
            self.backup_label.text = 'Backup created successfully!'
        except Exception as e:
            self.backup_label.text = 'Error during backup: ' + str(e)
            self.show_error_popup('Backup Error', 'Error during backup: ' + str(e))

    def restore_data(self, instance):
        # Restore data from the latest backup
        data_dir = 'data'
        backups = [f for f in listdir(data_dir) if f.startswith('backup_')]
        if not backups:
            self.restore_label.text = 'No backups found.'
            return

        latest_backup = max(backups, key=lambda x: path.getmtime(path.join(data_dir, x)))
        backup_path = path.join(data_dir, latest_backup)

        try:
            # Remove the current data directory
            rmtree(data_dir)
            # Copy the backup back to the data directory
            copytree(backup_path, data_dir)
            self.restore_label.text = 'Data restored successfully!'
        except Exception as e:
            self.restore_label.text = 'Error during restore: ' + str(e)
            self.show_error_popup('Restore Error', 'Error during restore: ' + str(e))

    def show_error_popup(self, title, message):
        # Show a popup with an error message
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# If the script is run directly, run the application
if __name__ == '__main__':
    DataBackupRestoreApp().run()