class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: handle empty input edge case
        if not nums:
            return 0
        
        # Step 2: convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: initialize max length
        longest = 0
        
        # Step 4: iterate through the set
        for num in num_set:
            # Step 5: check if this number is the START of a sequence
            # (i.e., num-1 is NOT in the set)
            if (num-1) not in num_set:
                # Step 6: count forward from this start
                current = num
                length = 1
                
                # Step 7: while the next number exists, extend
                while (current+1) in num_set:
                    current += 1
                    length += 1
                
                # Step 8: update longest if this run is bigger
                longest = max(longest,length)
        
        return longest
