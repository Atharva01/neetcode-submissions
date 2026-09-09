from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        # counter_s, counter_t = {}, {}

        # for i in range(len(s)):
        #     counter_s[s[i]] = 1 + counter_s.get(s[i],0)
        #     counter_t[t[i]] = 1 + counter_t.get(t[i],0)
        
        # for c in counter_s:
        #     if counter_s[c] != counter_t.get(c,0):
        #         return False
        # return True

