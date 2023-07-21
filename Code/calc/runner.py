import sys
from operations import adding, sub, mult, div


def main(a: int, b: int, op: str):
    if op == '+':
        print(adding(a, b))
    if op == '-':
        print(sub(a, b))
    if op == '*':
        print(mult(a, b))
    if op == '/':
        print(div(a, b))


if __name__ == "__main__":
    x, y, operation = sys.argv[1:]
    main(int(x), int(y), operation)
