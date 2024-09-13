#!/usr/bin/python3
"""
    The N queens game player programming
"""
from sys import argv


class Cheese:
    
    def __init__(self,size=4):
        self.board = None
        self.queens = []
        self.possibilities = []
        self.failed_paths = []
        self.N = size

    def check_collision(self, pos_x, pos_y):
        # vertical collision
        for x in self.queens:
            if x[1] == pos_y:
                return True
        # horizontal collision
        for x in self.queens:
            if x[0] == pos_x:
                return True
        # diagonal collision
        x, y = pos_x, pos_y
        while x >= 0 and y >= 0:
            if (x-1, y-1) in self.queens:
                return True
            else:
                x -= 1
                y -= 1
        x, y = pos_x, pos_y
        while x < self.N and y < self.N:
            if (x+1, y+1) in self.queens:
                return True
            else:
                x += 1
                y += 1
        x, y = pos_x, pos_y
        while x >= 0 and y < self.N:
            if (x-1, y+1) in self.queens:
                return True
            else:
                x -= 1
                y += 1
        x, y = pos_x, pos_y
        while x < self.N and y >= 0:
            if (x+1, y-1) in self.queens:
                return True
            else:
                x += 1
                y -= 1
        return False
    
    def back_propagation(self, row: int, col: int) -> bool:
        # TODO: Check ending conditions
        if row >= self.N or col >= self.N:
            return False
        if self.check_collision(pos_x=row, pos_y=col):
            print("Collision found ({}, {})".format(row, col))
            for i in  range(col, N):
                self.back_propagation(row, i)
        else:
            print("No Collision found ({}, {})".format(row, col))
            self.queens.append((row, col))
            self.back_propagation(row+1, col)
        if len(self.queens) == N:
            self.possibilities.append(self.queens.copy())
        else:
            self.failed_paths.append(self.queens.copy())
        if len(self.queens) > 0:
            self.queens.pop()
        
    def search_n_queens_dispositions(self):
        for col in range(self.N):
            self.queens = []
            self.back_propagation(0, col)
    
    @staticmethod
    def print_list_object(list_obj):
        print("Printing List object")
        for x in list_obj:
            print("{}".format(x))

    def __str__(self):
        string = "CHEESE BOARD INFOS\n"
        string += "\tBoard Size: {}\n".format(self.N)
        string += "\tACTUAL QUEENS DISPOSITIONS: {}\n".format(len(self.queens))
        for x in self.queens:
            string += "\t\t{}".format(x)
        string += "\n\tN-QUEENS DISPOSITIONS: {}\n".format(len(self.possibilities))
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
    
    print("=====================================")
    cheese.search_n_queens_dispositions()
    print("=====================================")
    print("{}".format(cheese))
    print("=====================================")
    print("{}".format(cheese.failed_paths[:50]))
    print("=====================================")
    cheese.print_list_object(cheese.failed_paths)
    print("=====================================")
