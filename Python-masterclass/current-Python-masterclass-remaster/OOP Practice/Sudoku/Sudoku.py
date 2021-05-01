def Invalid_index(r, c, ):
    try:
        var = board[r - 1][c - 1]
        return None
    except IndexError as i:
        if (c < 0 or c > 3) and (r < 0 or r > 3):
            print(f'{i} --> Column: {c} | Row: {r} --> Col and Row must be between 1-3')
            raise SystemExit
        elif c < 0 or c > 3:
            print(f'{i} --> Column: {c} --> Col must be between 1-3')
            raise SystemExit
        elif r < 0 or r > 3:
            print(f'{i} --> Row: {r} --> Row must be between 1-3')
            raise SystemExit


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

possible_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row, col, num = 0, 0, -1
check = None
while True:
    if check is None:
        if num in possible_inputs:
            if board[row - 1][col - 1] == 0:
                board[row - 1][col - 1] = num
                possible_inputs.remove(num)
                for row in board:
                    for col in row:
                        print(col, end='   ')
                    print('\n')
            else:
                print('The grid is occupied!')
                num = -1
        else:
            print(f'Please enter a number from {possible_inputs}')
            row = int(input('Row: '))
            col = int(input('Column: '))
            num = int(input('Enter the number: '))
            check = Invalid_index(row, col)

    ex = False
    for a in range(3):
        for b in range(3):
            if board[a][b] == 0:
                ex = True
                break
        break

    if not ex:
        break
