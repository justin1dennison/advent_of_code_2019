import fileinput
import math

def transform(weight):
    return math.floor(weight / 3.0) - 2


def main():
    total = 0
    for line in fileinput.input():
        weight = int(line)
        total += transform(weight)
    print(f'Total: {total}')


if __name__ == '__main__':
    main()
