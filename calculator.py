# Creating Command Line Utilities in Python::
# Creating command-line utilities in Python can be done using various libraries, but one of the most commonly used libraries is argparse, which is part of the Python standard library. argparse allows you to create user-friendly command-line interfaces with options, arguments, and help messages.


import argparse

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError
    return x / y

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.x, args.y)
    elif args.operation == "sub":
        result = sub(args.x, args.y)
    elif args.operation == "mul":
        result = mul(args.x, args.y)
    elif args.operation == "div":
        try:
            result = div(args.x, args.y)
        except ValueError as e:
            print(e)
            return

    print(f"Result of {args.operation}: {result}")

if __name__ == "__main__":
    main()



