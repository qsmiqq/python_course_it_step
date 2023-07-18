# work with sys.argv
import sys


# recursion
def fact(i):
    if i == 1:
        return i
    return i * fact(i - 1)


if __name__ == "__main__":
    print(fact(int(sys.argv[1])))
