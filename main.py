from src.stdin import output
from src.is_odd import is_odd
from src.division import division
from src.loop import exponential
from src import gregorian
from src import printter

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

if __name__ == '__main__':
    pass