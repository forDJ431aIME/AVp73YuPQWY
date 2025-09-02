# 代码生成时间: 2025-09-02 13:48:14
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
import os

# Define the supported file formats
SUPPORTED_FORMATS = {'.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                  '.pdf': 'application/pdf',
                  '.txt': 'text/plain'}

class ConverterPopup(Popup):
    '''Popup for document conversion'''
    def __init__(self, **kwargs):
        super(ConverterPopup, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.title = 'Document Converter'
        self.add_widget(self.layout)
        self.add_widgets()

    def add_widgets(self):
        self.layout.add_widget(Label(text='Select a file to convert'))
        self.source_file = Button(text='Choose Source File')
        self.source_file.bind(on_press=self.open_file_dialog)
        self.layout.add_widget(self.source_file)
        self.target_format = Button(text='Choose Target Format')
        self.target_format.bind(on_press=self.open_format_dialog)
        self.layout.add_widget(self.target_format)
        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert_file)
        self.layout.add_widget(self.convert_button)

    def open_file_dialog(self, instance):
        '''Open file dialog and set the source file path'''
        self.file_chooser = FileChooserPopup(select=self.select_file)
        self.file_chooser.open()

    def select_file(self, selection, selection_index, data):
        '''Callback for file selection'''
        self.source_file.text = f'Selected: {selection[0]}'
        self.source_file_path = selection[0]

    def open_format_dialog(self, instance):
        '''Open popup for selecting target format'''
        self.format_popup = Popup(title='Select Target Format', size_hint=(0.9, 0.6))
        self.format_popup.layout = BoxLayout(orientation='vertical')
        self.format_popup.add_widget(Label(text='Choose target format'))
        for ext, mime_type in SUPPORTED_FORMATS.items():
            button = Button(text=f'Convert to {ext}')
            button.bind(on_press=lambda btn, fmt=ext: setattr(self, 'target_format', fmt))
            self.format_popup.layout.add_widget(button)
        self.format_popup.open()

    def convert_file(self, instance):
        '''Convert the selected file to the chosen format'''
        if hasattr(self, 'source_file_path') and hasattr(self, 'target_format'):
            try:
                # Simulate file conversion
                # In a real application, you would call a conversion library or API here
                print(f'Converting {self.source_file_path} to {self.target_format} format...')
                # Update the UI to indicate conversion success
                self.dismiss()
                App.get_running_app().root.show_message('Conversion Successful', 'File converted successfully!')
            except Exception as e:
                # Handle conversion errors
                App.get_running_app().root.show_message('Conversion Failed', str(e))
        else:
            App.get_running_app().root.show_message('Error', 'Please select both source file and target format.')

    def show_message(self, title, message):
        '''Show a message to the user'''
        message_box = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(200, 200))
        message_box.open()

class DocumentConverterApp(App):
    '''Main Kivy application class'''
    def build(self):
        self.root = BoxLayout()
        self.root.add_widget(Button(text='Convert Document', on_press=self.open_converter_popup))
        return self.root

    def open_converter_popup(self, instance):
        '''Open the document conversion popup'''
        self.converter_popup = ConverterPopup()
        self.converter_popup.open()

if __name__ == '__main__':
    DocumentConverterApp().run()