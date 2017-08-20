# -*- coding: utf-8 -*-

name = 'glew'

version = '2.0.0'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
