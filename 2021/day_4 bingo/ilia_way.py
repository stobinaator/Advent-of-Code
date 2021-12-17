import os

RAW = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class BingoBoard:
    def __init__(self, board_config: str) -> None:
        """
        Creates a bingo board from a string config
        """
        board_as_str = [x.split() for x in board_config.splitlines()]
        self.board = [[int(x) for x in board_row] for board_row in board_as_str]
        self.recognized = [[False for x in board_row] for board_row in self.board]
        self.last_num = -1
        self.winning_num = -1
        self.won = False

    def _check_bingo(self) -> None:
        """
        Checks if the current board wins the game
        and updates self.won and self.winning_num
        """
        for row in self.recognized:
            if all(row):
                self.won = True
                self.winning_num = self.last_num

        for n_col in range(5):
            col = [x[n_col] for x in self.recognized]
            if all(col):
                self.won = True
                self.winning_num = self.last_num

    def add_number(self, number: int) -> bool:
        """
        Evaluates a new number and checks wether it wins the game
        """
        if not self.won:
            self.last_num = number
            for row in range(5):
                for col in range(5):
                    if self.board[row][col] == number:
                        self.recognized[row][col] = True
            self._check_bingo()

        return self.won

    def sum_unmarked(self) -> int:
        """
        Sum all unmarked numbers
        """
        total = 0
        for row in range(5):
            for col in range(5):
                if self.recognized[row][col] is False:
                    total += self.board[row][col]
        return total


if __name__ == "__main__":
    # Load input
    cd = os.path.abspath(os.getcwd())
    input = open(f"{cd}/input.txt").read()

    # Extract bingo numbers
    bingo_numbers = [int(x) for x in input.splitlines()[0].split(",")]

    # Extract the bingo configurations
    configurations = []
    for i in range(2, len(input.splitlines()), 6):
        configurations.append("\n".join(input.splitlines()[i : i + 5]))

    # Part 1
    boards = [BingoBoard(config) for config in configurations]

    done = False
    for n in bingo_numbers:
        for b in boards:
            bingo = b.add_number(n)
            if bingo:
                print(n * b.sum_unmarked())
                done = True
                break
        if done:
            break

    # Part 2
    boards = [BingoBoard(config) for config in configurations]
    winning_order = []
    for n in bingo_numbers:
        for i, b in enumerate(boards):
            won = b.add_number(n)
            if won and i not in winning_order:
                winning_order.append(i)

    last_won = boards[winning_order[-1]]

    print(last_won.winning_num * last_won.sum_unmarked())
