from typing import List

def escape(jar: List[int], fly: List[int]) -> bool:
    W, H, d = jar
    x0, y0, vx, vy = fly
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(escape([1000, 500, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 500, 200], [0, 0, 100, 0]) == False
    assert escape([1000, 500, 200], [450, 50, 0, -100]) == True
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
