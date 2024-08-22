def minimum_cost_to_limit_range(nums, n, k):
    nums.sort()
    
    def calculate_cost(low, high):
        total_cost = 0
        for num in nums:
            if num < low:
                total_cost += abs(num - low)
            elif num > high:
                total_cost += abs(num - high)
        return total_cost

    left, right = 0, max(nums) - min(nums)
    result = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        valid = False
        for i in range(n):
            if i + mid < n:
                low = nums[i]
                high = nums[i + mid]
                if high - low <= k:
                    valid = True
                    result = min(result, calculate_cost(low, high))
                    break
        if valid:
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