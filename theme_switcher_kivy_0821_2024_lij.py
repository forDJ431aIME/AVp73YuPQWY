# 代码生成时间: 2025-08-21 20:24:25
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
# 扩展功能模块
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


class ThemeButton(Button):
    """自定义按钮类，用于切换主题"""
    theme_color = StringProperty('1E90FF')  # 默认主题颜色

    def switch_theme(self):
        """切换主题颜色"""
        try:
# 改进用户体验
            # 尝试获取颜色值并转换为RGB格式
            color = get_color_from_hex(self.theme_color)
            Window.clearcolor = color  # 设置窗口背景色
        except ValueError:
            print("Invalid color value.")  # 错误处理


class ThemeSwitcherApp(App):
    """主应用程序类"""
    def build(self):
        """构建界面"""
        layout = BoxLayout(orientation='vertical')
        # 创建两个按钮，用于切换主题
        theme_button = ThemeButton(text='Switch to Blue Theme', theme_color='1E90FF')
        theme_button.bind(on_release=theme_button.switch_theme)
        layout.add_widget(theme_button)

        theme_button = ThemeButton(text='Switch to Green Theme', theme_color='32CD32')
        theme_button.bind(on_release=theme_button.switch_theme)
        layout.add_widget(theme_button)

        return layout


if __name__ == '__main__':
    ThemeSwitcherApp().run()