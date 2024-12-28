# -----------------------------------------#
# -- Speed Test App Based On Decorators -- #
# -----------------------------------------#

from time import time


def speedTest(func):
    def wrapper(*arg, **kwargs):
        start = time()
        func(*arg, **kwargs)
        end = time()
        print(f"{func.__name__} function Took {end - start} seconds")

    return wrapper


@speedTest
def passValues(n):
    for i in range(n):
        pass


passValues(1000000)
