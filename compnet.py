# -*- coding: utf-8 -*-
"""
计算图框架
"""

class Tensor(object):
    """
    must have shape, type for checker
    """
    pass

class Constant(Tensor):
    pass

class Variable(Tensor):
    pass

class PlaceHolder(Tensor):
    pass

"""
1. 如何构建计算图? ... python list!
["Operation", Tensor1, Tensor2, Tensor3...]
例子:
a = ["FC", W1, x, b1]
a_relu = ["RELU", a]
a2 = ["FC", W2, x, b2]
a2_relu = ["RELU", a2]
compose = ["CONCAT", a_relu, a2_relu]
out = ["FC", Wout, compose, 0]
loss = ["SOFTMAX_CROSSENTROPY", out, label]
"""

def compile_forward(*output_nodes):
    """
    分析图的拓扑结构，得到前向计算路径(后序遍历)
    例子:
    compiled = compile(loss, out)
    计算路径是如何表示的? ... python list
    声明共享的变量 (特殊操作 LET)
    [
        ["LET", "a", ["FC", W1, x, b1]],
        ["LET", ....],
        ["LET", ...],
        ["LET", ...],
        ["RETURN", out, loss]
    ]
    """
    pass

def compile_backward(loss_node):
    """
    分析图的拓扑结构，得到反向传播路径
    例子:
    compiled = compile(loss, out)
    计算路径是如何表示的? ... python list
    声明共享的变量 (特殊操作 LET)
    [
        ["LET", "a", ["FC", W1, x, b1]],
        ["LET", ....],
        ["LET", ...],
        ["LET", ...],
        ["RETURN", out, loss]
    ]
    """
    pass

def run(compiled, your_module):
    """
    利用你的上下文来运行这个计算图
    如果计算有定义 checker，就会先运行 checker
    """
    pass
