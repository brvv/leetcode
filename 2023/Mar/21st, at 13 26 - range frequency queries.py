#prefix elem num and postfix elem num for each value in arr
#the above is calculated during initialization
# use binary search to find start and end positions, do sum - (prefix[start] + postfix[end])
# building the data structure is O(unique(n)* 2), which is 10**4
# every query is log(vals) * 2

class RangeFreqCalculator:
    def __init__(self):
        self.indexes = []

    def addIndex(self, index):
        self.indexes.append(index)


    def query(self, left, right):
        left_point = bisect_left(self.indexes, left)
        right_point = bisect_right(self.indexes, right)

        return right_point - left_point



class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.dict = self.buildDict()

    def buildDict(self):
        self.dict = {}

        for i, val in enumerate(self.arr):
            if val not in self.dict:
                self.dict[val] = RangeFreqCalculator()
            (self.dict[val]).addIndex(i)
        
        return self.dict


    def query(self, left: int, right: int, value: int) -> int:
        if value in self.dict:
            return (self.dict[value]).query(left, right)
        else:
            return 0
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)