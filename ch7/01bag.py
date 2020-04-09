# 01背包问题
def bag(n, M, w, v):
    res = [[-1 for j in range(M+1)] for i in range(n+1)]
    for j in range(M+1):
        res[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, M+1):
            res[i][j] = res[i-1][j]
            if j >= w[i-1] and res[i][j] < res[i-1][j-w[i-1]]+v[i-1]:
                res[i][j] = res[i-1][j-w[i-1]]+v[i-1]
    return res


def show(n, M, w, res):
    print('Most Value:', res[n][M])
    x = [False for i in range(n)]
    j = M
    for i in range(1, n+1):
        if res[i][j] > res[i-1][j]:
            x[i-1] = True
            j -= w[i-1]
    print('selected objects:')
    for i in range(n):
        if x[i]:
            print('the', i, 'one,', end=' ')
    print("")
    for i in range(n):
        for j in range(M+1):
            print(res[i][j], end="\t")
        print()


if __name__ == '__main__':
    n = 7
    M = 15
    w = [2, 3, 5, 7, 1, 4, 1]
    v = [10, 5, 15, 7, 6, 18, 3]
    res = bag(n, M, w, v)
    show(n, M, w, res)
