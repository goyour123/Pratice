

import time

def measuretime(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (func.__name__, end - start)
        return result

    return wrapper

@measuretime
def count_down(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    count_down(500000)