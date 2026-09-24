import sys

def greet(name):
    return f"Hello, {name}! Welcome to Python {sys.version.split()[0]}."

if __name__ == "__main__":
    print(greet("Mohammad"))