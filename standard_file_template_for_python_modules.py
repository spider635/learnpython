#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行注释可以让这个文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码

# 任何模块代码的第一个字符串都被视为模块的文档注释
' a test module '

# 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
__author__ = 'Band Jia'

import sys

def _test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()
