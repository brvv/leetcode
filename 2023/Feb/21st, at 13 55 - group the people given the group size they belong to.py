class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)


        for person_i, size in enumerate(groupSizes):
            if size not in dic:
                dic[size].append([person_i])
            else:
                last_group = dic[size][-1]
                if len(last_group) < size:
                    dic[size][-1].append(person_i)
                else:
                    dic[size].append([person_i])
        
        res = []

        for groups in dic.values():
            for group in groups:
                res.append(group)
                    
        
        return res
