def solution(R, V):
    # 初始化银行 A 和 B 的余额
    balance_A = 0
    balance_B = 0

    # 记录银行 A 和 B 的最低余额
    min_balance_A = 0
    min_balance_B = 0

    # 遍历每个转账
    for i in range(len(R)):
        if R[i] == 'B':
            balance_A -= V[i]  # A 向 B 转账
            balance_B += V[i]
        else:
            balance_B -= V[i]  # B 向 A 转账
            balance_A += V[i]

        # 更新最低余额
        min_balance_A = min(min_balance_A, balance_A)
        min_balance_B = min(min_balance_B, balance_B)

    # 计算所需的初始余额
    initial_balance_A = -min_balance_A if min_balance_A < 0 else 0
    initial_balance_B = -min_balance_B if min_balance_B < 0 else 0

    return [initial_balance_A, initial_balance_B]

# 测试用例
print(solution("BAABA", [2, 4, 1, 1, 2]))  # 应该返回 [2, 4]
print(solution("ABAB", [10, 5, 10, 15]))  # 应该返回 [0, 15]
print(solution("B", [100]))  # 应该返回 [100, 0]