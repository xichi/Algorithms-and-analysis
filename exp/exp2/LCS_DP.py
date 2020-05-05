# 动态规划
# 自底而上


def LCS_dp(input_x, input_y):
    # input_x as column, input_y as row
    dp = [([0] * (len(input_y)+1)) for i in range(len(input_x)+1)]
    for i in range(1, len(input_x)+1):
        for j in range(1, len(input_y)+1):
            if input_x[i-1] == input_y[j-1]:  # 不在边界上，相等就加一
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 不相等
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for dp_line in dp:
        print(dp_line)
    return dp[-1][-1], dp

if __name__ == "__main__":
    a = 'bdcaba'
    b = 'abcbdab'
    lcs_length, dp = LCS_dp(a, b)
    print(lcs_length)
