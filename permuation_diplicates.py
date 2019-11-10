from itertools import permutations

class Solution:
    def permuteUnique_slow(self, nums):
        '''
        Permutation 排列，置换
        Get all possible unique permutations
        Args:
            nums: A collection of numbers that might contain duplicates
        Returns:
            answer: All possible unique permutations
        '''

        if len(nums) <= 1:
            return [nums]

        answer = []
        for i in range(len(nums)):
            n = nums[:i] + nums[i + 1:]
            for y in self.permuteUnique(n):
                new_permutation = [nums[i]] + y
                if new_permutation not in answer:
                    answer.append([nums[i]] + y)
        print('permutation', answer)
        return answer

    def permuteUnique(self, nums):
        answer = list(set([l for l in permutations(nums)]))
        print(answer)
        return answer

if __name__ == '__main__':
    nums = [1,1,2]
    output = Solution()
    output.permuteUnique(nums)