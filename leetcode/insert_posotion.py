class Solution:
    dup_mid = -1
    target = []
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        return self.find_index(0, len(nums))
        
    
    def find_index(self, start, end):
        mid = (end-start)//2+start
        
        if self.target > self.nums[end-1] and self.dup_mid <0:
            return end
        
        if self.target < self.nums[start] and self.dup_mid <0:
            return 0    
        
        if mid == self.dup_mid:
            return self.dup_mid +1

        if self.target > self.nums[mid]:
            self.dup_mid = mid
            return self.find_index(mid, end)

        if self.target < self.nums[mid]:
            self.dup_mid = mid
            return self.find_index(start, mid)
        
        if self.target == self.nums[mid]:
            return mid
        return -1