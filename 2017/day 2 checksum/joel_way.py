from typing import List

def to_rows(ss: str) -> List[List[int]]:
    rows = ss.split('\n')
    print(rows)
    rows = [[int(cell) for cell in row.split()] for row in rows]
    return rows

def checksum(ss: str) -> int:
    """
    for each row, find max - min, and add those up
    """
    rows = to_rows(ss)
    return sum(max(row) - min(row) for row in rows) 

test_ss = """5 1 9 5
7 5 3
2 4 6 8"""

assert checksum(test_ss) == 18

def row_dividend(row: List[int]) -> int:
    """
    There are exactly two values in the row for which one
    evenly divides the other. Return their quotient
    """
    for i, value in enumerate(row):
        for other_value in row[(i+1):]:
            if value % other_value == 0:
                return value // other_value
            elif other_value % value == 0:
                return other_value // value
    
    raise ValueError("no pair found")

def checksum_divisible(ss: str) -> int:
    rows = to_rows(ss)
    return sum(row_dividend(row) for row in rows)