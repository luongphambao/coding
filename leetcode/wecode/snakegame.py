EMPTY = '.'
BODY = '*'
DEAD = 'X'
HEADS = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}

def get_next(x, y, snake, gameBoard):
    for (dx, dy)  in HEADS.values():
        new_x, new_y = x + dx, y + dy
        if new_x in range(len(gameBoard)) and \
           new_y in range(len(gameBoard[0])) and \
           (new_x, new_y) not in snake and \
           gameBoard[new_x][new_y] == BODY:
            return (new_x, new_y)

def find_snake(gameBoard):
    # Get the head and the next body opposite of snake's direction
    snake = []
    for i, row in enumerate(gameBoard):
        for head, (dx, dy) in HEADS.items():
            if head in row:
                beginx, beginy = i, row.index(head)
                snake.append((beginx, beginy))
                snake.append((beginx - dx, beginy - dy))

    # Append the rest of the body
    while True:
        n = get_next(snake[-1][0], snake[-1][1], snake, gameBoard)
        if n is None:
            break
        snake.append(n)

    return snake

def move_snake(snake, gameBoard):
    headx, heady = snake[0]
    head = gameBoard[headx][heady]
    dx, dy = HEADS[head]
    new_x, new_y = headx + dx, heady + dy
    new_coord = new_x, new_y
    new_snake = []
    if new_x in range(len(gameBoard)) and \
       new_y in range(len(gameBoard[0])) and \
       new_coord not in snake:
        new_snake.append(new_coord)
        for pos in snake[:-1]:
            new_snake.append(pos)
        return new_snake


def snakeGame(gameBoard, commands):
    new_direc = {'v': {'L': '>', 'R': '<'}, 
                 '^': {'L': '<', 'R': '>'},                 
                 '<': {'L': 'v', 'R': '^'}, 
                 '>': {'L': '^', 'R': 'v'}}
    # Find starting snake
    snake = find_snake(gameBoard)

    for command in commands:   
        if command in "LR":
            # Change the head
            headx, heady = snake[0]
            gameBoard[headx][heady] = new_direc[gameBoard[headx][heady]][command]
        else:
            temp = move_snake(snake, gameBoard)

            # if not valid move return dead snake
            if temp is None:
                for (x, y) in snake:
                    gameBoard[x][y] = DEAD 
                return gameBoard

            # else move snake
            for a, b in zip(snake, temp):
                gameBoard[b[0]][b[1]] = gameBoard[a[0]][a[1]]

            tailx, taily = snake[-1]
            gameBoard[tailx][taily] = EMPTY 
            snake = temp

    return gameBoard
def test_snake(gameBoard, commands):
    out = snakeGame(gameBoard, commands)
    print(out, commands)
n, m, c = [int(i) for i in input().split()]
board = []
for h in range(n):
    l = list(i for i in input())
    board.append(l)
move = list(i for i in input())
test_snake(board,move)
        