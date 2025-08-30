# 代码生成时间: 2025-08-30 09:52:53
import kivy
from kivy.app import App
from kivy.uix.button import Button
# NOTE: 重要实现细节
from kivy.uix.boxlayout import BoxLayout
# 优化算法效率
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from Crypto.Cipher import AES
# 扩展功能模块
from Crypto.Util.Padding import pad, unpad
# 优化算法效率
from Crypto.Random import get_random_bytes
import base64

"""
密码加密解密工具的主程序，使用KIVY框架创建图形用户界面，
并利用AES算法进行密码加密和解密。
"""

class EncryptionDecryptionApp(App):
    def build(self):
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical')

        # 创建输入框
        self.input_text = TextInput(multiline=True, hint_text="Enter text...")
# 添加错误处理
        main_layout.add_widget(self.input_text)

        # 创建加密按钮
        encrypt_button = Button(text="Encrypt")
        encrypt_button.bind(on_press=self.encrypt)
        main_layout.add_widget(encrypt_button)

        # 创建解密按钮
        decrypt_button = Button(text="Decrypt")
        decrypt_button.bind(on_press=self.decrypt)
        main_layout.add_widget(decrypt_button)

        # 创建输出框
        self.output_text = Label(text="")
        main_layout.add_widget(self.output_text)

        return main_layout

    def encrypt(self, instance):
        """加密文本。"""
# TODO: 优化性能
        try:
            key = get_random_bytes(16)  # 生成16字节的随机密钥
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(self.input_text.text.encode(), AES.block_size))
            iv = base64.b64encode(cipher.iv).decode('utf-8')
            ct = base64.b64encode(ct_bytes).decode('utf-8')
            encrypted_message = iv + ct
# 扩展功能模块
            self.output_text.text = "Encrypted: " + encrypted_message
        except Exception as e:
            self.output_text.text = "Encryption error: " + str(e)

    def decrypt(self, instance):
        """解密文本。"""
        try:
            encrypted_message = self.input_text.text
            iv = base64.b64decode(encrypted_message[:16])
            ct = base64.b64decode(encrypted_message[16:])
            cipher = AES.new(get_random_bytes(16), AES.MODE_CBC, iv)  # 这里需要保存iv, key
# 优化算法效率
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            self.output_text.text = "Decrypted: " + pt.decode('utf-8')
        except Exception as e:
            self.output_text.text = "Decryption error: " + str(e)

if __name__ == '__main__':
    EncryptionDecryptionApp().run()