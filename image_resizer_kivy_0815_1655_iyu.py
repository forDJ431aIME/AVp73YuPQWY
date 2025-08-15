# 代码生成时间: 2025-08-15 16:55:49
import os
from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from PIL import Image
import shutil

"""
Image Resizer Kivy Application
This program allows users to select multiple images and resize them to a specified dimension.
"""

class ImageResizerApp(App):
# 增强安全性
    def build(self):
        return ImageResizerLayout()

class ImageResizerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
# 优化算法效率
        self.orientation = "vertical"
        self.add_widget(Label(text="Select Images"))
        self.image_chooser = FileChooserListView()
        self.image_chooser.filters = ["*.jpg", "*.png"]
        self.add_widget(self.image_chooser)
        self.add_widget(Button(text="Resize Images", on_press=self.resize_images))
# 添加错误处理
        self.status_label = Label(text="")
        self.add_widget(self.status_label)

    def resize_images(self, instance):
        selected_paths = self.image_chooser.selection
        if not selected_paths:
            self.status_label.text = "No images selected."
            return

        try:
            width, height = map(int, self.get_resize_dimensions())
# 增强安全性
        except ValueError:
            self.status_label.text = "Invalid dimensions."
            return

        for image_path in selected_paths:
            try:
                self.resize_image(image_path, width, height)
                self.status_label.text = f"Resized {os.path.basename(image_path)}."
            except Exception as e:
# 扩展功能模块
                self.status_label.text = f"Error resizing {os.path.basename(image_path)}: {str(e)}"

    def get_resize_dimensions(self):
        # This function should be implemented to prompt the user for new dimensions
# 增强安全性
        # For simplicity, we'll assume the dimensions are hardcoded
        return 800, 600  # Example dimensions

    def resize_image(self, image_path, width, height):
# 添加错误处理
        with Image.open(image_path) as img:
            img = img.resize((width, height), Image.ANTIALIAS)
# TODO: 优化性能
            base, ext = os.path.splitext(image_path)
            new_path = f"{base}_resized{ext}"
            img.save(new_path)
            shutil.copymode(image_path, new_path)  # Preserve file permissions

if __name__ == "__main__":
    ImageResizerApp().run()
