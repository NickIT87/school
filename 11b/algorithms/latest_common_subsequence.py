def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    # Створення матриці для збереження результатів
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Заповнення матриці знизу вгору
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Відновлення найдовшої спільної підпослідовності
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)


# Приклад використання
str1 = "ABCBDAB"
str2 = "BDCAB"

result = longest_common_subsequence(str1, str2)
print("Найдовша спільна підпослідовність:", result)
