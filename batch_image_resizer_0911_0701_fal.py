# 代码生成时间: 2025-09-11 07:01:47
import os
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from PIL import Image
from PIL import ImageOps
import threading
"""
Batch Image Resizer
This application allows users to select multiple images and resize them to a specified dimension.
"""

class ImageResizerApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Add file chooser for selecting images
        self.file_chooser = FileChooserListView(
            rootpath=os.path.expanduser('~'),
            filters=['*.jpg', '*.png', '*.gif', '*.bmp'],
            size_hint=(1, 0.6),
            multiselect=True
        )
        main_layout.add_widget(self.file_chooser)
        
        # Add popup for resize settings
        self.resize_popup = Popup(
            title='Resize Settings',
            content=BoxLayout(orientation='vertical'),
            size_hint=(None, None),
            size=(300, 200)
        )
        self.resize_popup.content.add_widget(Label(text='Width:'))
        self.resize_width = TextInput(text='100')
        self.resize_popup.content.add_widget(self.resize_width)
        self.resize_popup.content.add_widget(Label(text='Height:'))
        self.resize_height = TextInput(text='100')
        self.resize_popup.content.add_widget(self.resize_height)
        self.resize_popup.content.add_widget(Button(text='Resize', on_press=self.resize_images))
        self.resize_popup.dismiss()
        
        # Add button for opening resize settings
        resize_button = Button(text='Resize Images')
        resize_button.bind(on_press=self.open_resize_popup)
        main_layout.add_widget(resize_button)
        
        return main_layout
    
    def open_resize_popup(self, instance):
        self.resize_popup.open()
    
    def resize_images(self, instance):
        try:
            width = int(self.resize_width.text)
            height = int(self.resize_height.text)
        except ValueError:
            self.show_error_popup('Invalid dimensions', 'Width and height must be integers.')
            return
        
        selected_images = self.file_chooser.selection
        if not selected_images:
            self.show_error_popup('No images selected', 'Please select at least one image to resize.')
            return
        
        for image_path in selected_images:
            try:
                with Image.open(image_path) as img:
                    resized_img = ImageOps.fit(img, (width, height), Image.ANTIALIAS)
                    resized_img.save(image_path)
            except IOError:
                self.show_error_popup('Error resizing image', f'Failed to resize {image_path}')
    
    def show_error_popup(self, title, message):
        error_popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(200, 100))
        error_popup.open()

def main():
    ImageResizerApp().run()

def resize_thread(target_width, target_height, image_paths):
    try:
        for image_path in image_paths:
            with Image.open(image_path) as img:
                resized_img = ImageOps.fit(img, (target_width, target_height), Image.ANTIALIAS)
                resized_img.save(image_path)
    except Exception as e:
        print(f'Error resizing image: {e}')

def threaded_resize_images(width, height, image_paths):
    thread = threading.Thread(target=resize_thread, args=(width, height, image_paths))
    thread.start()

if __name__ == '__main__':
    main()