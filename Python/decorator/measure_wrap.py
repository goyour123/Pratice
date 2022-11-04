
import time
from functools import wraps

def measuretime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (func.__name__, end - start)
        return result

    return wrapper

@measuretime
def count_down(n):
    '''Counts down from n'''
    print (f'Counts down from {n}')
    while n > 0:
        n -= 1

if __name__ == '__main__':
    count_down(500000)
    print(count_down.__name__)
    print(count_down.__doc__)
    org_count_down = count_down.__wrapped__
    org_count_down(500000)
