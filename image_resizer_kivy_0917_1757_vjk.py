# 代码生成时间: 2025-09-17 17:57:15
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from PIL import Image
from PIL.ImageOps import fit
import shutil

# 文件选择对话框
class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
# 优化算法效率
        super(FileChooserPopup, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
# 改进用户体验
        self.filechooser = FileChooserListView()
        self.layout.add_widget(self.filechooser)

        self.ok_button = Button(text='Resize')
        self.ok_button.bind(on_release=self.resize_images)
        self.layout.add_widget(self.ok_button)

        self.cancel_button = Button(text='Cancel')
# 扩展功能模块
        self.cancel_button.bind(on_release=self.dismiss)
        self.layout.add_widget(self.cancel_button)

    def resize_images(self, instance):
        # 获取选中的文件路径
        selected_files = self.filechooser.selection
        for file_path in selected_files:
            try:
                self.resize_image(file_path)
            except Exception as e:
                # 显示错误信息
                self.dismiss()
                error_popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(200, 100))
# FIXME: 处理边界情况
                error_popup.open()
# 优化算法效率

    def resize_image(self, file_path):
        # 打开图片
        with Image.open(file_path) as img:
            # 调整图片尺寸
            resized_img = fit(img, (800, 600), Image.ANTIALIAS)
            # 保存调整后的图片
            new_file_path = os.path.join(os.path.dirname(file_path), f'resized_{os.path.basename(file_path)}')
            resized_img.save(new_file_path)

# 主应用
class ImageResizerApp(App):
    def build(self):
# 增强安全性
        self.title = 'Image Resizer'
        self.layout = BoxLayout(orientation='vertical', padding=10)
        self.layout.add_widget(Label(text='Select images to resize'))
# 添加错误处理

        self.select_button = Button(text='Select Images')
        self.select_button.bind(on_release=self.open_file_chooser)
        self.layout.add_widget(self.select_button)
# 增强安全性

        return self.layout
# 改进用户体验

    def open_file_chooser(self, instance):
# NOTE: 重要实现细节
        file_chooser_popup = FileChooserPopup()
        file_chooser_popup.open()

    def on_stop(self):
        # App关闭时清理
# FIXME: 处理边界情况
        pass

# 应用入口
# 改进用户体验
if __name__ == '__main__':
    ImageResizerApp().run()
