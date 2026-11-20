import sys


if __name__ == "__main__":
    print(sum(int(value) for value in sys.argv[1:]))
