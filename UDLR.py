TC = int(input())
ans = []
for tc in range(1, TC+1):
    k = "#" + str(tc) + " "
    N = int(input())
    X, Y = 1, 1
    plans = input().split()

    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계회을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = X + dx[i]
                ny = Y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        X, Y = nx, ny
    k += str(X) + " " + str(Y)
    ans.append(k)
for e in ans:
    print(e)