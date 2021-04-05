from collections import deque
n, m, c = [int(i) for i in input().split()]
board = []
for h in range(n):
    l = list(i for i in input())
    board.append(l)
move = list(i for i in input())
class Snake:
    def __init__(self):
        def createSnake(snake, i,j):
            temp = deque()
            temp.append((i, j - 1))
            temp.append((i, j + 1))
            temp.append((i - 1, j))
            temp.append((i + 1, j))
            while temp:
                if temp[0][0] < 0 or temp[0][0] >= n or temp[0][1] < 0 or temp[0][1] >= m:
                    temp.popleft()
                elif board[temp[0][0]][temp[0][1]] == '.':
                    temp.popleft()
                elif (temp[0][0],temp[0][1]) in snake:
                    temp.popleft()
                else:
                    break
            if len(temp) == 0:
                return (-1, -1)
            return (temp[0][0],temp[0][1])

        self.snake = deque()
        for i in range(n):
            for j in range(m):
                if board[i][j] in ['<','^','>','v']:
                    self.snake.append((i,j))
                    break
            if len(self.snake) != 0:
                break
        i,j = self.snake[0][0], self.snake[0][1]
        self.state = board[i][j]
        while True:
            i,j = createSnake(self.snake,i,j)
            if (i,j) == (-1,-1):
                break
            self.snake.append((i,j))
    def TurnRight(self):
        if self.state == '<':
            self.state = '^'
        elif self.state == '^':
            self.state = '>'
        elif self.state == '>':
            self.state = 'v'
        else: self.state = '<'
    def TurnLeft(self):
        if self.state == '<':
            self.state = 'v'
        elif self.state == 'v':
            self.state = '>'
        elif self.state == '>':
            self.state = '^'
        else: self.state = '<'
    def Forward(self):
        def Dead(snake, i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return True
            if (i,j) in snake:
                return True
            return False
        i, j = -1, -1
        if self.state == '<':
            i, j = self.snake[0][0], self.snake[0][1] - 1
        elif self.state == '^':
            i, j = self.snake[0][0] - 1, self.snake[0][1]
        elif self.state == '>':
            i, j = self.snake[0][0], self.snake[0][1] + 1
        elif self.state == 'v':
            i, j = self.snake[0][0] + 1, self.snake[0][1]
        if not Dead(self.snake, i, j):
            self.snake.appendleft((i,j))
            self.snake.pop()
            return 1
        else: return 0
    def DrawAlive(self):
        for i in range(n):
            for j in range(m):
                if (i,j) not in self.snake:
                    board[i][j] = '.'
                else:
                    if (i,j) == (self.snake[0][0], self.snake[0][1]):
                        board[i][j] = snake.state
                    else: board[i][j] = '*'
    def DrawDead(self):
        for i in range(n):
            for j in range(m):
                if (i,j) not in self.snake:
                    board[i][j] = '.'
                else:
                    board[i][j] = 'X'
    def Move(self, move):
        for i in move:
            if i == 'F':
                if self.Forward() == 0:
                    self.DrawDead()
                    return
            elif i == 'L':
                self.TurnLeft()
            else:
                self.TurnRight()
        self.DrawAlive()
if __name__ == "__main__":
    snake = Snake()
    snake.Move(move)
    for i in board:
        for j in i:
            print(j,end='')
        print('')