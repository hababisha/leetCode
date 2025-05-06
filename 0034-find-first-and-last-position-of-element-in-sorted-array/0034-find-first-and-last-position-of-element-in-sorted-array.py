class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        l = 0 
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                ans[0] = mid
                r = mid - 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        i = 0 
        j = len(nums) -1
        while i <= j:
            middle = i + (j-i) // 2
            if nums[middle] == target:
                ans[1] = middle
                i = middle + 1
            elif target < nums[middle]:
                j = middle - 1
            else:
                i = middle + 1
        return ans