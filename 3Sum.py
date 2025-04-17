# sort the array
# -nums[i] = nums[j] + nums[k]
# now it's a problem where num[j] + nums[k] = target. where (target = -nums[i])
# using two pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array, O(nlogn)
        nums.sort()
        for i, ele in enumerate(nums):
            # since the array is sorted, if ele > 0, then there will never be nums[i] + nums[j] + nums[k] == 0 because nums[i] has to be negative
            if ele > 0:
                break
            # check duplicate: if it's not the first ele and it is the same value as the ele before
            if i > 0 and ele == nums[i - 1]:
                continue
            # We use two pointers:
            # l (left pointer) starts just after i
            # r (right pointer) starts at the end of the array
            # These pointers will move inward to find pairs that sum to -a.
            l, r = i + 1, len(nums) - 1
            # O(n^2)
            while l < r:
                threeSum = ele + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    #save the valid triplets
                    res.append([ele, nums[l], nums[r]])
                    # to explore the other opportunities without duplicates
                    l += 1
                    r -= 1
                    # skips duplicate, [-2, -2, 0, 0, 2, 2]
                    while l < r and nums[r] == nums[r + 1] and nums[l] == nums[l - 1] :
                        l += 1
                        
        return res
   