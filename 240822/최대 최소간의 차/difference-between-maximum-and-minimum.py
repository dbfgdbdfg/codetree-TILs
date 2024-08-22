def minimum_cost_to_limit_range(nums, n, k):
    nums.sort()

    # 비용 계산 함수
    def calculate_cost(target):
        cost_increase = 0
        cost_decrease = 0

        for num in nums:
            if num < target:
                cost_increase += target - num
            elif num > target + k:
                cost_decrease += num - (target + k)

        return max(cost_increase, cost_decrease)

    left, right = 0, max(nums)
    result = float('inf')

    while left <= right:
        mid = (left + right) // 2
        current_cost = calculate_cost(mid)

        result = min(result, current_cost)

        # 이진 탐색 범위 조정
        if calculate_cost(mid) <= calculate_cost(mid + 1):
            right = mid - 1
        else:
            left = mid + 1

    return result

# 입력 받기
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 최소 비용 계산
min_cost = minimum_cost_to_limit_range(nums, n, k)
print(min_cost)