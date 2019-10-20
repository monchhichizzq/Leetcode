'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
range: [−2^31,  2^31 − 1] ([−214783648, 214783647]). For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        '''
        Reverse the input integer
        :param x: input integer
        :return:
                reversed integer
        '''

        num = 0

        # return the absolute value of a number
        a = abs(x)

        while(a!=0):
            # 123
            # a = 123
            # num = 0
            # First iteration
            # a = 12
            # num = 3
            # second iteration
            # a = 1
            # num = 32
            # Third iteration
            # a = 0
            # num = 321
            # 除余运算
            temp = a % 10
            num = num * 10 + temp
            # a = int(a/10)
            # or
            a = a // 10

        if x > 0 and num < 2147483647:
            print(num)
        elif x < 0 and num <= 2147483647:
            print(-num)
        else:
            print(0)


if __name__ == '__main__':

    x_1 = 32111
    x_2 = -2213
    x_3 = 0
    output = Solution()
    output.reverse(x_1)
    output.reverse(x_2)
    output.reverse(x_3)