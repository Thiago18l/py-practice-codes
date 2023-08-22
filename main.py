from src.stdin import output
from src.is_odd import is_odd
from src.division import division
from src.loop import exponential
from src import gregorian
from src import printter
from src import list_comprehensions
from src import score


def main():
    a = int(input().strip())
    b = int(input().strip())
    output(a, b)

    # Is_Odd
    n = int(input().strip())
    is_odd(n)

    # Division
    a = int(input().strip())
    b = int(input().strip())
    division(a, b)

    #Loop
    n = int(input().strip())
    exponential(n)

    year = int(input().strip())
    gregorian.calendar(year)

    printter(3)

    list_comprehensions._list(x=1, y=1, z=2, n=3)
    score.score_(5, [2, 3, 5, 5, 6])

if __name__ == '__main__':
    pass