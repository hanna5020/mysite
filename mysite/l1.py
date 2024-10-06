def solution(A):
    n = len(A)
    if n < 2:
        return 0

    sum_positions = {}
    max_count = 0

    for i in range(n - 1):
        segment_sum = A[i] + A[i + 1]
        if segment_sum not in sum_positions:
            sum_positions[segment_sum] = []
        sum_positions[segment_sum].append(i)

    for positions in sum_positions.values():
        count = 1
        last_pos = positions[0]
        for pos in positions[1:]:
            if pos > last_pos + 1:
                count += 1
                last_pos = pos
        max_count = max(max_count, count)

    return max_count


# 定义测试函数
def test_solution():
    # 测试用例 1
    A1 = [10, 1, 3, 1, 2, 2, 1, 0, 4]
    print(f"Test 1 - Expected: 3, Got: {solution(A1)}")

    # 测试用例 2
    A2 = [5, 3, 1, 3, 2, 3]
    print(f"Test 2 - Expected: 1, Got: {solution(A2)}")

    # 测试用例 3
    A3 = [9, 9, 9, 9, 9]
    print(f"Test 3 - Expected: 2, Got: {solution(A3)}")

    # 测试用例 4
    A4 = [1, 5, 2, 4, 3, 3]
    print(f"Test 4 - Expected: 3, Got: {solution(A4)}")

    # 边界情况 1：空数组
    A5 = []
    print(f"Test 5 - Expected: 0, Got: {solution(A5)}")

    # 边界情况 2：长度为 1 的数组
    A6 = [1]
    print(f"Test 6 - Expected: 0, Got: {solution(A6)}")

    # 边界情况 3：只有两个元素
    A7 = [1, 2]
    print(f"Test 7 - Expected: 1, Got: {solution(A7)}")

    # 测试用例 5：所有元素和都相等
    A8 = [3, 3, 3, 3, 3, 3]
    print(f"Test 8 - Expected: 5, Got: {solution(A8)}")

# 运行测试
test_solution()
