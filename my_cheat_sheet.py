


# add import path
import sys
sys.path.append("/Users/DWDSamuelson/Desktop/datacapturing/lib")

# key listener, key input
def key_listener():
    from pynput import keyboard

    def on_press(key):
        print(key)

    with keyboard.Listener(on_press=on_press) as listener:
        pass


# terminal notifier
def notify(title, subtitle='', message='', group=None, timeout=None):
    import os

    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    o = '-group ID {!r}'.format('msg')
    out = t + ' ' + s + ' ' + m + ' '
    if group:
        out += '-group ID {!r}'.format(group)
    if timeout:
        out += 'timeout {!r}'.format('msg')

    os.system('terminal-notifier {}'.format(' '.join([out])))
    # terminal-notifier for more commands


def decorator(function):
    """prints hello first"""
    from functools import wraps

    @wraps(function)
    # keeps the metadata of the function to be decotarted, otherwise it will take metadata from my_wrapper
    def my_wrapper(function):

        print("hello")
        function()
    return my_wrapper


@decorator
def foo():
    """prints this is foo"""
    print("this is foo")
# print (foo.__name__) is still foo because of @wraps

# function timer, time


def time_function(some_function):  # decorates function with timer
    import time

    def wrapper():
        t1 = time.time()
        out = some_function()
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)))
        return out
    return wrapper

# self, class, cls, static method


class types_of_methods():

    def __init__(self, arg):
        self.data = arg

    def __repr__(self):  # runs at instantiaion (dundr) , sould return class info back to init call
        return(str(self.data))

    def function(self):
        print('function')

    def method(self):
        self.data  # can access class data
        self.func()  # can access methods
        internal_instance = self.__class__(786)  # self can access class

    @classmethod
    def class_method(cls):
        print('test')
        # cls.func()  # can't access class data but can access methods

        # return ['test_return']
        # return cls(['test_return'])  # not sure the difference

    @staticmethod
    def staticmethod_(inp):
        print(inp)  # has no access to the class


types_of_methods.class_method()  # class method can be called without an instance if the method doesnt use an instance
# print(types_of_methods(12))  # repr response
# instance = types_of_methods(22)

# instance.func()  #can be called like this
# types_of_methods.func(instance) #or like this
# print (instance.class_method())

# multi dim arr subarray


def subarray_of_multi_dim_array():
    import numpy as np
    arr = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]])
    arr = arr[:, :, 0:3]
    print(arr)
    #[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]
