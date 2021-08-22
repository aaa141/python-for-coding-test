# https://www.acmicpc.net/problem/3190
n = int(input())
k = int(input())
board = [[0]*n for i in range(n)] # 보드판, 사과 갯수
snake = [[0]*n for i in range(n)] # 뱀이 위치한 곳.
snake[0][0] = 1

for i in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

move = [[0, -1],[1, 0],[0, 1],[-1, 0]] # 0, 90, 180, 270
point = 1 # 현재 이동방향 ex. move[1]
# L = -90 : -1 , D = +90 : +1

c = int(input())  # 뱀의 방향 변환 횟수
change = []*c
for i in range(c):
    sec, d = input().split()
    if d == 'D': d = 1
    if d == 'L': d = -1
    change.append([int(sec), d])
change.append([0, 0])

time = 0
x, y = 0, 0 # 현재 위치
while True:
    time += 1
    # 이동할 칸
    if time == change[0][0]:  # 이동방향 바뀌었을 때
        point = abs(point+change[0][1]) % 4
        change.pop()
    ox, oy = x + move[point][0], y + move[point][1]

    # 벽에 부딪혔는지 검사
    if ox >= n or oy >= n:
        break

    # 자기 자신과 부딪혔는지 검사
    if snake[ox][oy] == 1:
        break
    # 사과가 있는지 검사
    snake[ox][oy] = 1
    if board[ox][oy] == 1: # 사과 먹고 몸 늘리기
        board[ox][oy] = 0
    else: # 몸 길이 유지 = 꼬리 자르기
        for i in range(n):
            for k in range(n):
                if snake[i][k] == 1:
                    snake[i][k] = 0

    x, y = ox, oy

print(time+1)
