# 代码生成时间: 2025-08-05 20:47:49
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.core.window import Window
import shutil
import glob


# 批量文件重命名工具类
class BatchRenameToolApp(App):
    def build(self):
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text="批量文件重命名工具"))
        
        # 创建文件浏览器
        self.file_chooser = FileChooserListView()
        self.layout.add_widget(self.file_chooser)
        
        # 创建按钮
        self.rename_button = Button(text='重命名')
        self.rename_button.bind(on_release=self.rename_files)
        self.layout.add_widget(self.rename_button)
        
        # 创建状态标签
        self.status_label = Label(text='')
        self.layout.add_widget(self.status_label)
        
        return self.layout
    
    # 重命名文件的函数
    def rename_files(self, instance):
        try:
            # 获取选中的文件
            selected_files = self.file_chooser.selection
            if not selected_files:
                self.status_label.text = '请先选择文件'
                return
            
            # 获取重命名规则
            rename_rule = self.get_rename_rule()
            if not rename_rule:
                return
            
            # 重命名文件
            for file_path in selected_files:
                # 构造新文件名
                new_file_name = self.construct_new_filename(file_path, rename_rule)
                # 重命名
                self.rename_file(file_path, new_file_name)
            
            # 更新状态
            self.status_label.text = '重命名完成'
        except Exception as e:
            self.status_label.text = '发生错误：' + str(e)
    
    # 获取重命名规则
    def get_rename_rule(self):
        # 这里可以添加文件名规则输入的逻辑
        # 例如弹出输入框让用户输入规则
        # 这里直接返回一个简单的规则作为示例
        return 'new_{}'
    
    # 构造新文件名
    def construct_new_filename(self, file_path, rename_rule):
        # 提取文件扩展名
        _, ext = os.path.splitext(file_path)
        # 构造新文件名
        new_file_name = rename_rule.format(os.path.basename(file_path)) + ext
        # 返回新文件名
        return new_file_name
    
    # 重命名文件
    def rename_file(self, file_path, new_file_name):
        # 构造新文件路径
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        # 重命名文件
        shutil.move(file_path, new_file_path)
        
# 运行程序
if __name__ == '__main__':
    BatchRenameToolApp().run()
