class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We could use a similar approach as 'Valid Anagram' and just bruteforce for each n in strs
        final = []
        for string in strs:
            group = []
            for lol in strs:
                if sorted(string) == sorted(lol):
                    group.append(lol)
            if group not in final:
                final.append(group)
        return final
        