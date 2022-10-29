def greet(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper

@greet
def say_hello(name):
    print(f"Hello {name}")

if __name__ == '__main__':
    say_hello('Alice')
    say_hello('Bob')