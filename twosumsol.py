# LeetCode: Two Sum
# Difficulty: Easy
# Focus: Python basics, dictionary usage

def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i
        print(f"Seen dict updated: {seen}")

nums = [1, 5, 3, 8, 15]
target = 9

result = twoSum(nums, target)
print(result)

