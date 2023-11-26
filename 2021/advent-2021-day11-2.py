DATA_TEST = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]
DATA = [
    "6111821767",
    "1763611615",
    "3512683131",
    "8582771473",
    "8214813874",
    "2325823217",
    "2222482823",
    "5471356782",
    "3738671287",
    "8675226574",
]


def run(data):
    results = 0
    board = []
    for row in data:
        board.append([int(x) for x in row])

    for row in board:
        print(row)

    step = 1
    while True:
        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] += 1

        step_flash = check_board(board)

        results += step_flash

        # for row in board:
        #     print(row)

        all_sum = sum(sum(board, []))
        if all_sum == 0:
            return step
        print(f"{step}: {all_sum}")
        step += 1

    return


def check_board(board):
    step_flash = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            me = board[row][col]
            if me > 9:
                step_flash += 1
                board[row][col] = 0
                if row > 0 and col > 0:
                    if board[row - 1][col - 1] != 0:
                        board[row - 1][col - 1] += 1
                if row > 0:
                    if board[row - 1][col] != 0:
                        board[row - 1][col] += 1
                if row > 0 and col < len(board[0]) - 1:
                    if board[row - 1][col + 1] != 0:
                        board[row - 1][col + 1] += 1
                if col > 0:
                    if board[row][col - 1] != 0:
                        board[row][col - 1] += 1
                if col < len(board[0]) - 1:
                    if board[row][col + 1] != 0:
                        board[row][col + 1] += 1
                if row < len(board) - 1 and col > 0:
                    if board[row + 1][col - 1] != 0:
                        board[row + 1][col - 1] += 1
                if row < len(board) - 1:
                    if board[row + 1][col] != 0:
                        board[row + 1][col] += 1
                if row < len(board) - 1 and col < len(board[0]) - 1:
                    if board[row + 1][col + 1] != 0:
                        board[row + 1][col + 1] += 1

    if step_flash > 0:
        return step_flash + check_board(board)
    else:
        return 0


if __name__ == "__main__":
    results = run(DATA)
    print(results)
