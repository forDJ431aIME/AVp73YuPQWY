# 代码生成时间: 2025-10-08 20:20:51
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import requests

# 药物相互作用检查类
class DrugInteractionChecker(BoxLayout):
    def __init__(self, **kwargs):
        super(DrugInteractionChecker, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # 创建界面元素
        self.drug1_input = TextInput(hint_text='Enter drug 1', multiline=False)
        self.drug2_input = TextInput(hint_text='Enter drug 2', multiline=False)
        self.check_button = Button(text='Check Interaction')
        self.result_label = Label(text='')
        
        # 添加界面元素到布局
        self.add_widget(self.drug1_input)
        self.add_widget(self.drug2_input)
        self.add_widget(self.check_button)
        self.add_widget(self.result_label)
        
        # 绑定按钮事件
        self.check_button.bind(on_press=self.check_interaction)
        
    def check_interaction(self, instance):
        # 获取用户输入的药物名称
        drug1 = self.drug1_input.text.strip()
        drug2 = self.drug2_input.text.strip()
        
        # 检查输入是否为空
        if not drug1 or not drug2:
            self.show_error_popup('Both drugs must be entered.')
            return
        
        # 调用API检查药物相互作用
        try:
            response = requests.get('https://api.example.com/interaction', params={'drug1': drug1, 'drug2': drug2})
            response.raise_for_status()
            result = response.json()
            
            # 显示检查结果
            self.result_label.text = result.get('message', 'No interaction found.')
        except requests.exceptions.RequestException as e:
            self.show_error_popup(f'Error checking interaction: {e}')
        
    def show_error_popup(self, message):
        # 显示错误信息
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# Kivy应用类
class DrugInteractionApp(App):
    def build(self):
        return DrugInteractionChecker()

# 主程序入口
if __name__ == '__main__':
    DrugInteractionApp().run()