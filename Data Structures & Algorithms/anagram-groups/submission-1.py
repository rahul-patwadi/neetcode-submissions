class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
    
        for s in strs:
            # Step 1: create a count array of size 26
            
            # (one slot for each letter a-z)
            count = [0]*26
        
            # Step 2: for each character in s,
            # increment the right position
            for c in s:
                count[ord(c)-ord('a')] += 1
        
        # Step 3: use count as key, append s to that group
            d[tuple(count)].append(s)
    
        return list(d.values())