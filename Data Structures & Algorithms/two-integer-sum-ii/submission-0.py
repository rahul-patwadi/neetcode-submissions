class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1  # last index
        
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed!
            elif current_sum < target:
                left += 1  # move left
            else:
                right -=1  # move right
        
        return []  # not strictly needed but safe
        