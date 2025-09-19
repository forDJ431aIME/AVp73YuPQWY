# 代码生成时间: 2025-09-20 00:20:33
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from cryptography.fernet import Fernet

# 密码加密解密应用
class PasswordEncryptionDecryptionApp(App):
    def build(self):
        # 创建布局
        layout = BoxLayout(orientation='vertical')
        # 创建输入框
        self.password_input = TextInput(multiline=False)
        layout.add_widget(self.password_input)
        # 创建显示框
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)
        # 创建加密按钮
        encrypt_button = Button(text="Encrypt")
        encrypt_button.bind(on_press=self.encrypt_password)
        layout.add_widget(encrypt_button)
        # 创建解密按钮
        decrypt_button = Button(text="Decrypt")
        decrypt_button.bind(on_press=self.decrypt_password)
        layout.add_widget(decrypt_button)
        return layout
    
def generate_key():
    # 生成密钥
    return Fernet.generate_key()
    
def load_key():
    # 加载密钥，这里假设密钥保存在文件中
    with open("key.key", "rb") as key_file:
        return key_file.read()
    
def save_key(key):
    # 保存密钥到文件
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
def encrypt_password(instance, value):
    # 加密密码
    key = load_key()
    if key:
        try:
            cipher_suite = Fernet(key)
            encrypted_password = cipher_suite.encrypt(instance.password_input.text.encode()).decode()
            instance.result_label.text = "Encrypted: " + encrypted_password
        except Exception as e:
            instance.result_label.text = "Encryption Error: " + str(e)
    else:
        instance.result_label.text = "Key not found. Generate a new key."
    
def decrypt_password(instance, value):
    # 解密密码
    key = load_key()
    if key:
        try:
            cipher_suite = Fernet(key)
            decrypted_password = cipher_suite.decrypt(instance.password_input.text.encode()).decode()
            instance.result_label.text = "Decrypted: " + decrypted_password
        except Exception as e:
            instance.result_label.text = "Decryption Error: " + str(e)
    else:
        instance.result_label.text = "Key not found. Generate a new key."
    
def create_key_button(instance, value):
    # 创建密钥按钮
    key = generate_key()
    save_key(key)
    instance.result_label.text = "Key generated and saved."
    
def main():
    # 运行应用
    PasswordEncryptionDecryptionApp().run()
    """
    密码加密解密工具应用的主函数，负责运行Kivy应用。
    """
if __name__ == "__main__":
    main()