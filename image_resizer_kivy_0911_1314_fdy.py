# 代码生成时间: 2025-09-11 13:14:27
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from PIL import Image
import datetime

"""
ImageResizerKivyApp: A Kivy application to batch resize images.
"""

class ImageResizerKivyApp(App):
    def build(self):
        # Create a box layout for the main interface
        layout = BoxLayout(orientation='vertical')
        
        # Create a file chooser for selecting the directory
        self.filechooser = FileChooserListView(
            dirselect=True,
            filters=['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp'],
            path=os.path.join(os.path.expanduser('~'), 'Pictures')
        )
        layout.add_widget(self.filechooser)
        
        # Create a label to display the selected directory
        self.label = Label(text='Select a folder')
        layout.add_widget(self.label)
        
        # Create a button to start the resizing process
        resize_button = Button(text='Resize Images')
        resize_button.bind(on_press=self.resize_images)
        layout.add_widget(resize_button)
        
        return layout
    
    def update_label(self, selection):
        # Update the label with the selected directory
        if selection:
            self.label.text = 'Selected folder: ' + selection[0]
    
    def resize_images(self, instance):
        # Get the selected directory
        selected_folder = self.filechooser.selection
        if not selected_folder:
            self.show_error_popup('No folder selected')
            return
        
        # Resize images in the selected directory
        self.resize_images_in_folder(selected_folder[0])
    
    def resize_images_in_folder(self, folder_path):
        # Iterate over all image files in the folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.resize_image(os.path.join(folder_path, filename))
    
    def resize_image(self, image_path):
        try:
            # Open the image file
            with Image.open(image_path) as img:
                # Resize the image to 50% of its original size
                resized_img = img.resize((int(img.width / 2), int(img.height / 2)))
                # Save the resized image with a timestamp in the filename
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                resized_image_path = image_path.replace(
                    os.path.basename(image_path),
                    f'{timestamp}_{os.path.basename(image_path)}'
                )
                resized_img.save(resized_image_path)
                print(f'Resized image saved to: {resized_image_path}')
        except IOError as e:
            self.show_error_popup(f'Error resizing image {image_path}: {e}')
    
    def show_error_popup(self, message):
        # Show an error popup with the given message
        content = Label(text=message)
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(200, 200))
        popup.open()

if __name__ == '__main__':
    ImageResizerKivyApp().run()
