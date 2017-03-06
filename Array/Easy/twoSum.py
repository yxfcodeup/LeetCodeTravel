"""

 Description:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

 Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""

class Solution(object) :
    """
    : type nums: List[int]
    : type target: int
    : rtype: List[int]
    """
    def twoSum(self , nums , target) :
        half_target = int(target  / 2)
        len_nums = len(nums)
        half_index = int(len_nums / 2)
        top = len_nums
        bot = 0
        while True :
            if target > nums[half_index] and target <= nums[half_index + 1] :
                break
            elif target < nums[half_index] :
                top = half_index
                half_index = int((bot + half_index) / 2)
            elif target > nums[half_index + 1] :
                bot = half_index + 1
                half_index = int((top + half_index) / 2)
        print(half_index)
        while True :
            pass


if __name__ == "__main__" :
    s = Solution()
    s.twoSum([0, 2, 6, 7, 8, 11, 15] , 9)

