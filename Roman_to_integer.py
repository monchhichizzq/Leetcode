class Solution:
    def single(self, num, order, numeral_map, result_):

        num_ = (num - (num // order) * order)
        if num_ // (order / 10) <= 3:
            result = numeral_map[order // 10] * (num_ * 10 // order)
        elif 3 < num_ // (order / 10) <= 5:
            result = numeral_map[order //10] * (5 - num_*10 // order) + numeral_map[5*order//10]
        elif 5 < num_ // (order / 10) <= 8:
            result = numeral_map[5*order//10] + numeral_map[order //10] * (num_*10// order - 5)
        elif 8 < num_ // (order / 10) <= 10:
            result = numeral_map[order //10] * (10 - num_*10 // order) + numeral_map[order]
        if result_:
            result_ = result_ + result
        else:
            result_ = result
        return result_


    def intToRoman(self, num):
        '''
        integer to Roman
        num : integer input
        return:
                results: Roman output
        '''

        '''
        1826
        1 : len(1826) = 4 r = M
        8 : len = 3 if 8 > 5:
                    r = M-(10-8) 
                 else:
                    r = V-(5-8)
        2: len = 2 if 2 > 5:
                    r = M-(10-2) 
                 else:
                    r = V-(5-2)
        6: len = 1 if 6 > 5:
                        r = M-(10-6) 
                    else:
                        r = V-(5-6)
        '''
        numeral_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        print(num,len(str(num)))
        result = []
        int_len = len(str(num))
        for i in range(int_len):
            if int_len - i == 4:
                result = numeral_map[1000]*(num//1000)
            if int_len - i == 3:
                result = self.single(num, 1000, numeral_map, result)
            if int_len - i == 2:
                result = self.single(num, 100, numeral_map, result)
            if int_len - i == 1:
                result = self.single(num, 10, numeral_map, result)
        print(result)





if __name__ == '__main__':

    num = 1998
    output = Solution()
    output.intToRoman(num)
