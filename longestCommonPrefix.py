class Solution:
    def longestCommonPrefix(self, strs):
        '''
        To find the longest common prefix string amongst an array of strings
        Args:
            strs: input array of strings
        Return:
            result = the longest common prefix string
        '''
        if not strs:
            return ""

        for i in range(len(strs[0])):
            # 计算第一个string长度，与之后的单词逐个字母去比较
            # str[0][i] ?= strs[1][i]
            # 做循环提取list 后面部分的string
            for string in strs[1:]:
                # 如果list后面选取的string中有到第i位与第一个string不同
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]

        # [""] - indeed have a string, string = ""
        return strs[0]

    def optimisation_longestCommonPrefix(self, strs):
        '''
       To find the longest common prefix string amongst an array of strings
       Args:
           strs: input array of strings
       Return:
           result = the longest common prefix string
        '''
        result = ""
        i = 0

        # try except异常处理的方式
        # try 开始以后在python程序中做一些标记， 如果出现异常时就返回到异常处

        while True:
            try:

                # a = set('boy') -> set(['y', 'b', 'o'])
                # 集合add 是把要传入的元素做为一个整个添加到集合中
                # a.add('python') -> set(['y', 'python', 'b', 'o'])
                # 集合update方法：是把要传入的元素拆分，做为个体传入到集合中
                # a.update('python') -> set(['b', 'h', 'o', 'n', 'p', 't', 'y'])
                # 集合删除操作方法：remove
                # a.remove('python') -> set(['y', 'b', 'o'])

                # strs 中不重复的值有哪些， set 的返回值为各string中出现的不同字母
                sets = set(string[i] for string in strs)
                print('sets', sets)
                # 如果各个string中出现的不同字母 大于2， break
                if len(sets) == 1:
                    # pop 随机删除一个元素 sets.pop()为此被删除的元素
                    result += sets.pop()
                    i += 1
                else:
                    break
            # 常规错误积累 如果出现错误直接break
            except Exception as e:
                break
        return result


if __name__ == '__main__':
    List_1 = ["flower","flow","flight"]
    List_2 = [""]
    output = Solution()
    output_1 = output.optimisation_longestCommonPrefix(List_1)
    output_2 = output.longestCommonPrefix(List_2)
    print('output_1', output_1)
    print('output_2', output_2)