
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''



class Solution:
    def twoSum_1(self, nums, target):
        '''
        Args:
            type nums: List[int]
            type target: int
            rtype: List[int]
        Return:
            indices_list
        '''
       # test 1
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                index_start = nums.index(i)
                index_end = next_index + temp_nums.index(j)
                print(index_start, index_end)


    def twoSum_2(self, nums, target):
        '''
        Args:
            type nums: List[int]
            type target: int
            rtype: List[int]
        Return:
            indices_list
        '''
       # test 2
        dict = {}

        for i in range(len(nums)):
            # target = 9, the two numbers should all be in dict
            # put the nums[i] into the dict first, if there is the number (+nums[i]=9), output nums[i]_index and number_index
            if target - nums[i] not in dict:
                dict[nums[i]]= i
                print(dict)
            else:
                print(dict[target - nums[i]], i)





if __name__ == '__main__':

    List = [2, 7, 11, 15, 3, 6]
    target = 9
    output = Solution()
    output.twoSum_1(List, target)
    output.twoSum_2(List,target)

