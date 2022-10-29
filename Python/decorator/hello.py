
def hello_alice(hello_func):
    hello_func("Alice")

def say_hello(name):
    print (f"Hello {name}")

if __name__ == '__main__':
    hello_alice(say_hello)
