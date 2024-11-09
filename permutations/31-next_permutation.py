class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first_decreasing = -1

        for i in range(len(nums)-2, -1, -1):
            print(nums[i])
            if nums[i] < nums[i+1]:
                first_decreasing = i
                break
        
        if first_decreasing == -1:
            nums.sort()
            return

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[first_decreasing]:
                found = i
                break

        print(nums[first_decreasing], nums[found])
        nums[found], nums[first_decreasing] = nums[first_decreasing], nums[found]
        nums[first_decreasing+1:] = reversed(nums[first_decreasing+1:])

