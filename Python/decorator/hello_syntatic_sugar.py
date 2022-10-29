
def hello_alice(hello_func):
    hello_func("Alice")

@hello_alice
def say_hello(name):
    print (f"Hello {name}")

if __name__ == '__main__':
    say_hello
