class Solution:
    def twoSum(a,nums,target):
      seen={}
      for i ,num in enumerate(nums):
        complement=target-num 
        if complement in seen:
          return [seen[complement],i]
    
        seen[num]=i


##time complexity=O(n)
##space complexity=O(n)