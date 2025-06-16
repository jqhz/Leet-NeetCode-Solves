class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set() # initializes the set. this could alternatively just be an array[], and change the add() method to append()
        for n in nums: 
            if n in s: # if a number, n, has already been seen before (indicated by it existing in the set)
                return True
            s.add(n) # if a number is not already in the set, add it to the set. 
        return False
