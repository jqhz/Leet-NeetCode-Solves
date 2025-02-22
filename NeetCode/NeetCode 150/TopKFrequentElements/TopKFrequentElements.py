class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # looking back to basic DSA, bucket sort semi directly correlates to frequency
        
        count = {}
        freq = [[] for i in range(len(nums)+1)] # creates list holding len(nums+1) empty lists
        # so if nums = [1,1,1,2]
        # len(nums)+1 = 5
        # freq will have indexes, 0 1 2 3 4
        for num in nums:
            count[num] = 1+count.get(num,0)
            # key [num] gets maped to 1+count.get(num,0)
        #so our count set will have 
        '''
        1:3
        2:1
        '''
        for n,c in count.items(): #count 
            freq[c].append(n)
        #3: [1]

        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
# Solution uses bucket sort O(n)