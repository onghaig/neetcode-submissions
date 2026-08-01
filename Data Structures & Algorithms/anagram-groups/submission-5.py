from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # encode each string into a frozenset
        htable = defaultdict(list)
        for s in strs:
            htable["".join(sorted(s))].append(s)
        ret = []
        for key,value in htable.items():
            ret.append(htable.get(key))
        return ret