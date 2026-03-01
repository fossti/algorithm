def find_one_solution(n: int):
    pos = [-1] * n
    col_used = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row: int) -> bool:
        if row == n:
            return True
        for col in range(n):
            d1 = row + col
            d2 = row - col + (n - 1)
            if col_used[col] or diag1[d1] or diag2[d2]:
                continue
            pos[row] = col
            col_used[col] = diag1[d1] = diag2[d2] = True
            if backtrack(row + 1):
                return True
            col_used[col] = diag1[d1] = diag2[d2] = False
            pos[row] = -1
        return False

    if not backtrack(0):
        return None

    board = []
    for r in range(n):
        c = pos[r]
        board.append("." * c + "Q" + "." * (n - c - 1))
    return board


N = int(input())
board = find_one_solution(N)

if board is None:
    print("[]")
else:
    if N == 1:
        print('["Q"]')
    else:
        print('["' + board[0] + '",')
        for i in range(1, N - 1):
            print('"' + board[i] + '",')
        print('"' + board[N - 1] + '"]')