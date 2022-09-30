class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i]
            else:
                dic[num].append(i)
        for num in dic.keys():
            second_num = target - num
            
            if second_num in dic and not second_num == num:
                return [dic[num][0], dic[second_num][0]]
            elif second_num == num:
                if (len(dic[num])) > 1:
                    return dic[num][0:2]
            else:
                continue