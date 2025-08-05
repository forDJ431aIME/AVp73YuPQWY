# 代码生成时间: 2025-08-06 06:00:50
import psutil
# 优化算法效率
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
# TODO: 优化性能
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

"""
Process Manager Application using Python and Kivy Framework.
Allows users to view, terminate processes.
"""

class ProcessItem(BoxLayout):
# 扩展功能模块
    process_name = Label(text='', size_hint_y=None)
    process_pid = Label(text='', size_hint_y=None)
    terminate_button = Button(text='Terminate')

    def terminate_process(self):
        """
        Terminate the process associated with this item.
        """
        try:
            process = psutil.Process(self.pid)
            process.terminate()
            self.process_name.text = 'Terminating...'
            self.terminate_button.disabled = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f'Error terminating process: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.terminate_process()
            return True
        return super().on_touch_up(touch)

class ProcessManagerApp(App):
# 添加错误处理
    processes = ListProperty()

    def build(self):
        """
        Build the main application layout.
        """
        self.load_processes()
        return ScrollView(do_scroll_x=False)

    def load_processes(self):
        """
        Load a list of all running processes into the application.
        """
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process = proc.info
                self.processes.append(ProcessItem(pid=process['pid'],
                                            process_name=Label(text=process['name'],
                                                size_hint_y=None),
                                            process_pid=Label(text=str(process['pid']),
                                                size_hint_y=None),
                                            terminate_button=Button(text='Terminate',
                                                size_hint_y=None)))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f'Error loading processes: {e}')
            except Exception as e:
# 增强安全性
                print(f'An unexpected error occurred: {e}')

    def build_main_layout(self):
        """
        Build the main layout for displaying processes.
        """
# 添加错误处理
        main_layout = GridLayout(cols=1)
# 添加错误处理
        for process in self.processes:
            process.layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            process.process_name.size_hint = 0.5
            process.process_pid.size_hint = 0.2
            process.terminate_button.size_hint = 0.3
            process.process_name.bind(on_ref_press=self.on_process_name_press)
            process.terminate_button.bind(on_press=process.terminate_process)
            process.layout.add_widget(process.process_name)
            process.layout.add_widget(process.process_pid)
            process.layout.add_widget(process.terminate_button)
            main_layout.add_widget(process.layout)
        return main_layout

    def on_process_name_press(self, instance):
        """
        Handle process name press event (not implemented).
        """
        pass

if __name__ == '__main__':
    ProcessManagerApp().run()