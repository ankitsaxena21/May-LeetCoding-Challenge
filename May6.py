class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        items = set()
        for i in nums[1:]:
            if i not in items:
                items.add(i)
                if(nums.count(i) > nums.count(ans)):
                    ans = i
        return ans
        
