#!/usr/bin/python3
"""
    The N queens game player programming
"""
from sys import argv
from typing import List, Union


class Point:
    """ A position in the chesse game """
    def __init__(self, x: int, y: int) -> None:
        self.xpos = x
        self.ypos = y
        self.code = [self.ypos, self.xpos]

    def horizontal_alignment(self, point) -> bool:
        """ Check if two poins are horizontally aligned """
        if self.xpos == point.xpos:
            return True
        return False

    def vertical_alignment(self, point) -> bool:
        """ Check if two poins are vertically aligned """
        if self.ypos == point.ypos:
            return True
        return False

    def diagonal_alignment(self, point) -> bool:
        """ Check if two poins are horizontally aligned """
        if abs(self.xpos - point.xpos) == abs(self.ypos - point.ypos):
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.code}"

    def __str__(self) -> str:
        return f"[{self.ypos}, {self.xpos}]"


class Cheese:
    """ The chese class """
    board: List[List[Point]]
    queens: List[Point]
    possibilities: List[List[Point]]
    failed_paths: List[Point]
    N: int

    def __init__(self, size=4):
        """ Initialisation of the chese board """
        self.N = size
        self.board = []
        self.queens = []
        self.possibilities = []
        self.failed_paths = []

    def check_queen_insertion_collision(self, point: Point) -> bool:
        """ Collision checking """
        # vertical collision
        for x in self.queens:
            if point.vertical_alignment(x):
                return True
            elif point.horizontal_alignment(x):
                return True
            elif point.diagonal_alignment(x):
                return True
        return False

    def back_propagation(self, col: int, row: int) -> Union[bool, None]:
        """ Analysing each possibility """
        if col >= self.N or row >= self.N:
            return True
        for i in range(col, self.N):
            point = Point(x=i, y=row)
            if not self.check_queen_insertion_collision(point=point):
                self.queens.append(point)
                self.back_propagation(col=0, row=row+1)
        if len(self.queens) == self.N:
            self.possibilities.append(self.queens.copy())
        else:
            self.failed_paths.append(self.queens.copy())
        if len(self.queens) > 0:
            self.queens.pop()

    def search_n_queens_dispositions(self):
        """ Searching n queens function parser """
        for x in range(0, self.N):
            self.queens = []
            self.back_propagation(col=x, row=0)
        if self.N % 2 == 0:
            self.possibilities.pop(0)

    @staticmethod
    def print_list_object(list_obj: List):
        """ Printing the list of the queens """
        for x in list_obj:
            print("{}".format(x))

    def __str__(self):
        """ Stringifying """
        string = "CHEESE BOARD INFOS\n"
        string += "\tBoard Size: {}\n".format(self.N)
        string += "\tACTUAL QUEENS DISPOSITIONS: {}\n".format(len(self.queens))
        for x in self.queens:
            string += "\t\t{}".format(x)
        string += "\n\tN-QUEENS DISPOSITIONS: {}\n".format(
            len(self.possibilities))
        for x in self.possibilities:
            string += "\t\t{}".format(x)
        string += "\n\tFAILED: {}\n".format(len(self.failed_paths))
        for x in self.failed_paths:
            string += "\t\t{}\n".format(x)
        return string.strip()


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    cheese = Cheese(size=N)
    # print("=====================================")
    cheese.search_n_queens_dispositions()
    # print("=====================================")
    # print("{}".format(cheese))
    # print("=====================================")
    # print("{}".format(cheese.failed_paths[:50]))
    # print("=====================================")
    cheese.print_list_object(cheese.possibilities)
    # print("=====================================")
