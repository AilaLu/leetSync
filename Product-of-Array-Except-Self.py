class Solution:
    #make it into a busproblem of 1. return an array answer such that answer[i] is equal to the product of all the elements on the left
    #2. return an array answer such that answer[i] is equal to the product of all the elements on the right
    #combine the 1. and 2. 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        leftProduct = 1 
        for i in range(len(nums)):
            res[i] = leftProduct
            leftProduct *= nums[i]

        rightProduct = 1 
        for i in range(len(nums)-1, -1, -1):
            # combine left with right by multiply
            res[i] *= rightProduct
            rightProduct *= nums[i]


        return res
        
