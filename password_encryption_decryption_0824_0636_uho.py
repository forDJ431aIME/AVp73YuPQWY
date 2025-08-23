# 代码生成时间: 2025-08-24 06:36:50
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# 导入加密解密库
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class EncryptionDecryptionApp(App):"""
密码加密解密应用
"""
    def build(self):
        # 创建布局
        layout = BoxLayout(orientation='vertical')

        # 创建文本输入框
        self.input_text = TextInput(text='', multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.input_text)

        # 创建加密按钮
        self.encrypt_button = Button(text='Encrypt')
        self.encrypt_button.bind(on_press=self.encrypt)
        layout.add_widget(self.encrypt_button)

        # 创建解密按钮
        self.decrypt_button = Button(text='Decrypt')
        self.decrypt_button.bind(on_press=self.decrypt)
        layout.add_widget(self.decrypt_button)

        # 创建结果显示区域
        self.result_text = TextInput(multiline=True, size_hint=(1, 0.5), readonly=True)
        layout.add_widget(self.result_text)

        return layout

    def encrypt(self, instance):
        """
        加密函数
        """
        try:
            # 获取输入的文本
            input_text = self.input_text.text

            # 生成密钥
            key = get_random_bytes(16)

            # 创建加密器
            cipher = AES.new(key, AES.MODE_CBC)

            # 加密文本
            encrypted_text = cipher.encrypt(pad(input_text.encode(), AES.block_size))

            # 将密钥和加密文本一起显示
            self.result_text.text = f'Key: {key.hex()}
Encrypted Text: {encrypted_text.hex()}'
        except Exception as e:
            self.result_text.text = f'Error: {str(e)}'

    def decrypt(self, instance):
        """
        解密函数
        """
        try:
            # 获取输入的文本
            input_text = self.result_text.text

            # 解析密钥和加密文本
            key_hex, encrypted_text_hex = input_text.split('Encrypted Text: ')[0].split('Key: ')[-1], input_text.split('Encrypted Text: ')[-1]
            key = bytes.fromhex(key_hex)
            encrypted_text = bytes.fromhex(encrypted_text_hex)

            # 创建解密器
            cipher = AES.new(key, AES.MODE_CBC, cipher.iv)
            cipher.iv = key[:16]

            # 解密文本
            decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)

            # 显示解密结果
            self.result_text.text = f'Decrypted Text: {decrypted_text.decode()}'
        except Exception as e:
            self.result_text.text = f'Error: {str(e)}'


if __name__ == '__main__':
    EncryptionDecryptionApp().run()