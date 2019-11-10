class Solution:
    def isValid(self, s):
        '''
        To determine whether an input string is valid:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
        Args:
            s: input string
        Returns:
            bool: True or False
        '''
        stack = []
        lookup = {'(': ')', '{': '}', '[': ']'}

        for parenthese in s:
            print('parenthese', parenthese)

            if parenthese in lookup:
                stack.append(parenthese)
            # {[]}
            # [{]}
            # pop 是删除左边第一个 只要打出来就删除
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
            print('stack', stack)
        return len(stack) == 0

    def iteration(self, s):
        '''

        :param s:
        :return:
        '''
        stack = []
        lookup = {'(': ')', '{': '}', '[': ']'}

        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
            print('stack', stack)
        return len(stack) == 0



if __name__ ==  '__main__':
    s = "()[]{}"
    output = Solution()
    bool = output.iteration(s)
    print("()[]{}", bool)