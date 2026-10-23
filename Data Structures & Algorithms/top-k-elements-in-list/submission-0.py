class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers={}
   
        for num in nums:
          
            if num not in numbers:
              numbers[num]=1
            else:
              numbers[num]+=1
            
        sortn=sorted(numbers, key=numbers.get,reverse=True)
        return sortn[:k]
            
        