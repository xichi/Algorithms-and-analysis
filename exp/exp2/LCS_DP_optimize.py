def LCS(s1, s2):
    # s1 as column, s2 as row
    size1 = len(s1) + 1
    size2 = len(s2) + 1
    # 程序多加一行，一列，方便后面代码编写
    chess = [[["", 0] for j in list(range(size2))] for i in list(range(size1))]
    for i in list(range(1, size1)):
        chess[i][0][0] = s1[i - 1]
    for j in list(range(1, size2)):
        chess[0][j][0] = s2[j - 1]
    print("Init Data: ")
    for chess_line in chess:
        print(chess_line)
    for i in range(1, size1):
        for j in range(1, size2):
            if s1[i - 1] == s2[j - 1]:
                chess[i][j] = ['UL', chess[i - 1][j - 1][1] + 1]
            elif chess[i][j - 1][1] > chess[i - 1][j][1]:
                chess[i][j] = ['L', chess[i][j - 1][1]]
            else:
                chess[i][j] = ['U', chess[i - 1][j][1]]
    print("Computed: ")
    for chess_line in chess:
        print(chess_line)
    i = size1 - 1
    j = size2 - 1
    s3 = []
    while i > 0 and j > 0:
        if chess[i][j][0] == 'UL':
            s3.append(chess[i][0][0])
            i -= 1
            j -= 1
        if chess[i][j][0] == 'L':
            j -= 1
        if chess[i][j][0] == 'U':
            i -= 1
    s3.reverse()
    print("The longest common subsequence is: %s" % ''.join(s3))


if __name__ == "__main__":
    LCS("BDCABA", "ABCBDAB")
