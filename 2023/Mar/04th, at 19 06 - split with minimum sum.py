class Solution:
    def splitNum(self, num: int) -> int:
        lst = [int(i) for i in str(num)]
        s_lst = sorted(lst,reverse=True)

        num1, num2 = [], []
        counter = 0

        while len(s_lst) > 0:
            val = s_lst.pop()
            if counter % 2 == 0:
                num1.append(str(val))
            else:
                num2.append(str(val))
            counter += 1

        num1 = int(''.join(num1))
        num2 = int(''.join(num2))

        return num1 + num2



