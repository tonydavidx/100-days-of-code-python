
import time


def delay_decorator(function):
    def wrapper():
        time.sleep(3)
        function()
    return wrapper


@delay_decorator
def say_hi():
    print('Hi there!')


def say_bye():
    print('Bye!')


say_hi()
say_bye()
