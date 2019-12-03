import fileinput
import math
from itertools import takewhile

def repeatedly(func, *args):
    result = func(*args)
    while True:
        yield result
        result = func(result)


def transform(weight):
    return math.floor(weight / 3.0) - 2


def main():
    total = 0
    for line in fileinput.input():
        initial_weight = int(line)
        weights = takewhile(lambda x: x > 0, repeatedly(transform, initial_weight)) 
        total += sum(weights)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
