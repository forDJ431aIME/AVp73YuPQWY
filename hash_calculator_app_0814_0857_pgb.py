# 代码生成时间: 2025-08-14 08:57:32
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import hashlib

"""
哈希值计算工具，使用Python和Kivy框架创建。
""""

class HashCalculatorApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')
        
        # 输入框，用于输入需要计算哈希值的文本
        self.input_text = TextInput(multiline=False, hint_text='Enter text to hash')
        layout.add_widget(self.input_text)
        
        # 按钮，点击后计算哈希值
        calculate_button = Button(text='Calculate Hash', on_press=self.calculate_hash)
        layout.add_widget(calculate_button)
        
        # 标签，显示哈希值结果
        self.hash_result = Label(text='')
        layout.add_widget(self.hash_result)
        
        return layout
    
def calculate_hash(self, instance):
    # 获取输入框中的文本
    text_to_hash = self.input_text.text
    
    # 检查输入是否为空
    if not text_to_hash:
        self.hash_result.text = 'Please enter text to hash.'
        return
    
    try:
        # 计算哈希值
        # 使用SHA-256算法
        hash_object = hashlib.sha256(text_to_hash.encode())
        hash_hex = hash_object.hexdigest()
        
        # 显示结果
        self.hash_result.text = f'Hash (SHA-256): {hash_hex}'
    except Exception as e:
        # 错误处理
        self.hash_result.text = f'Error calculating hash: {str(e)}'
    

def main():
    HASH_CALCULATOR = HashCalculatorApp()
    HASH_CALCULATOR.run()
    
if __name__ == '__main__':
    main()
