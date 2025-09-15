# 代码生成时间: 2025-09-15 09:32:20
import requests
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.core.window import Window

class HttpRequestHandler:
    """HTTP请求处理器"""
    def __init__(self):
        # 初始化请求队列
        self.request_queue = []
        # 设置请求间隔时间（毫秒）
        self.request_interval = 1000
        
    def add_request(self, url, callback):
        """添加请求到队列"""
        self.request_queue.append((url, callback))
        
    def start(self):
        """开始处理请求"""
        # 如果队列非空，开始处理第一个请求
        if self.request_queue:
            self.process_request()
        else:
            Logger.info("HttpRequestHandler: Request queue is empty.")
        
    def process_request(self):
        """处理队列中的请求"""
        # 获取下一个请求
        url, callback = self.request_queue.pop(0)
        
        # 发起异步HTTP请求
        request = UrlRequest(url, on_success=self.on_request_success, on_error=self.on_request_error,
                              on_progress=self.on_request_progress, on_redirect=self.on_request_redirect,
                              req_kwargs={'timeout': 5})
        request.uid = callback  # 缓存回调函数
        
        # 设置下一个请求的计时器
        Clock.schedule_once(self.schedule_next_request, self.request_interval / 1000)
        
    def schedule_next_request(self, *args):
        """调度下一个请求"""
        # 如果队列非空，处理下一个请求
        if self.request_queue:
            self.process_request()
        else:
            Logger.info("HttpRequestHandler: Request queue is empty.")
    
    def on_request_success(self, request, result):
        """请求成功回调"""
        callback = request.uid
        if callback in self.request_queue:
            callback(result)
        else:
            Logger.info(f"HttpRequestHandler: Callback {callback} not found.")
        
    def on_request_error(self, request, error):
        "