class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set() # Creates HashSet
        for i in nums:
            if i in hashmap:
                return True
            # If does not exist in map (meaning not a duplicate)
            hashmap.add(i)
        # If it reaches here, it means that no duplicate was found in List 'nums'
        return False