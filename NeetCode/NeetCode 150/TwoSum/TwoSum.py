class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Target is what we are looking for
        storemap = {} # index -> value
        for i,v in enumerate(nums): # i represents index, v represents value
            complement = target - v   
            if complement in storemap: # Since our hashmap checks for key:value pairs
                return [storemap[complement],i] 
            storemap[v] = i # If complement is not found, add Value:Index, where Value is the Key, and Index is the Value
            # The map stores complement as the key so that 'if complement in storemap' can properly use and compare the keys
        return []
            