class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # YOUR LINE: append length, then #, then the string itself
            result += (str(len(s))) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            # find position of '#' starting from i
            while s[j] != '#':
                j += 1
            
            # YOUR LINE: convert s[i:j] to an integer, that's the length
            length = int(s[i:j])
            
            # YOUR LINE: extract the actual string and add it to result
            result.append(s[j+1:j+1+length])
            
            # YOUR LINE: move i past the string we just extracted
            i = j + 1 + length
        return result
        