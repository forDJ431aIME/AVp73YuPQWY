# 代码生成时间: 2025-10-03 03:58:27
# 导入必要的库
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ListProperty
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from kivy.utils import get_color_from_hex_code

# 定义一个Kivy Widget，用于绘制神经网络
# 改进用户体验
class NeuralNetworkWidget(Widget):
    node_size = NumericProperty(100)  # 节点大小
    node_color = ListProperty(get_color_from_hex_code('#ff0000'))  # 节点颜色
    
    def __init__(self, model, **kwargs):
# 添加错误处理
        super(NeuralNetworkWidget, self).__init__(**kwargs)
        self.model = model  # 使用传入的神经网络模型
        self.canvas = self.canvas.before
        self.draw_network()
    
    # 绘制神经网络
    def draw_network(self):
        try:
            self.canvas.clear()
            layer_nodes = []
            
            # 遍历每一层
            for i, layer in enumerate(self.model.layers):
                if i == 0:
                    # 绘制输入层
                    layer_nodes = self.draw_layer(layer, layer_nodes, 0)
                else:
                    # 绘制隐藏层和输出层
                    layer_nodes = self.draw_layer(layer, layer_nodes, 1)

        except Exception as e:
            print(f"Error drawing neural network: {e}")
    
    # 绘制单个层
# NOTE: 重要实现细节
    def draw_layer(self, layer, layer_nodes, layer_type):
        nodes = []
        
        # 计算节点位置
        for j, node in enumerate(layer.output_shape[1:]):
            x = self.width * (j + 0.5) / (layer.output_shape[1] + 1)
            y = self.height * (i + 0.5) / (len(self.model.layers) + 1)
            
            # 绘制节点
            with self.canvas:
                Color(*self.node_color)
                Ellipse(pos=(x - self.node_size / 2, y - self.node_size / 2), size=(self.node_size, self.node_size))
                nodes.append((x, y))
            
        # 如果不是输入层，绘制连接线
# 添加错误处理
        if layer_type == 1:
            self.draw_connections(layer_nodes, nodes)
            
        return nodes
    
    # 绘制节点之间的连接线
    def draw_connections(self, layer_nodes, nodes):
        for i, node in enumerate(layer_nodes):
            for j, next_node in enumerate(nodes):
                with self.canvas:
                    Color(1, 1, 1, 0.5)  # 灰色连接线
                    Line(points=[node[0], node[1], next_node[0], next_node[1]], width=2)

# 定义一个Kivy App
class NeuralNetworkApp(App):
    def build(self):
        # 创建一个简单的神经网络模型
# TODO: 优化性能
        model = Sequential()
        model.add(Dense(64, activation='relu', input_shape=(784,)))
        model.add(Dense(10, activation='softmax'))
        
        # 返回神经网络可视化Widget
        return NeuralNetworkWidget(model)

# 运行Kivy App
if __name__ == '__main__':
    NeuralNetworkApp().run()