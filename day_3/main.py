from typing import List, Tuple, NewType, Generator, Any
from enum import Enum
import json
from collections import Counter

with open("./input.txt") as f:
    data = [line.strip() for line in f.readlines()]


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


Point = NewType("Point", Tuple[int, int])
Movement = NewType("Movement", Tuple[Direction, int])
Path = NewType("Path", List[Movement])


def movement(chunk: str) -> Movement:
    direction = Direction(chunk[0])
    amount = int(chunk[1:])
    return Movement((direction, amount))


def path(line: str) -> Path:
    chunks = line.split(",")
    return Path([movement(chunk) for chunk in chunks])


def positions(start: Point, path: Path) -> Generator[Point, Any, Any]:
    current = start
    for direction, amount in path:
        for i in range(1, amount + 1):
            x, y = current
            if direction == Direction.DOWN:
                point = Point((x, y - i))
            elif direction == Direction.LEFT:
                point = Point((x - i, y))
            elif direction == Direction.RIGHT:
                point = Point((x + i, y))
            else:
                point = Point((x, y + i))
            yield point
        current = point


def distance(point: Point, frm: Point = Point((0, 0))) -> float:
    dx, dy = point
    fx, fy = frm
    return abs(dx - fx) + abs(dy - fy)


def main():
    first, second = [path(line) for line in data]
    fpositions = set(positions(Point((0, 0)), first))
    spositions = set(positions(Point((0, 0)), second))
    intersections = fpositions & spositions
    distances = (distance(intersection) for intersection in intersections)
    print(f"Minimum Distance: {min(distances)}")


if __name__ == "__main__":
    main()
