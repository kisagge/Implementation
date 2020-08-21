TC = int(input())
ans = []
for tc in range(1, TC+1):
    k = "#" + str(tc) + " "
    h = int(input())

    cnt = 0
    for i in range(h + 1):
        for j in range(60):
            for p in range(60):
                if '3' in str(i) + str(j) + str(p):
                    cnt += 1
    k += str(cnt)
    ans.append(k)
for e in ans:
    print(e)