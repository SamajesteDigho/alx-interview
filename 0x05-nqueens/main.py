#!/usr/bin/python3

Point = __import__("0-nqueens").Point
Cheese = __import__("0-nqueens").Cheese
pp = Point(x=0, y=1)
p1 = Point(x=1, y=3)
p2 = Point(x=2, y=0)
p3 = Point(x=3, y=2)

cheese = Cheese(size=4)
cheese.queens = [p1, p2, p3]

print(cheese.check_queen_insertion_collision(pp))

# for x in [p1, p2, p3]:
#     print(f"{x} and {pp}")
#     print(f"\t{x} and {pp} are horizontally aligned: {pp.horizontal_alignment(x)}")
#     print(f"\t{x} and {pp} are vertically aligned: {pp.vertical_alignment(x)}")
#     print(f"\t{x} and {pp} are diagonally aligned: {pp.diagonal_alignment(x)}")
