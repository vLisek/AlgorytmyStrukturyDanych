def lcs3(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    dp = [[[0]*(n3+1) for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )

    print("Długość LCS-3:", dp[n1][n2][n3])
    return dp[n1][n2][n3]


s1 = "ABCD"
s2 = "ACBAD"
s3 = "ABAD"
lcs3(s1, s2, s3)
