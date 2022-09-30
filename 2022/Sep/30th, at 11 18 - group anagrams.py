class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dics = []
        res = []
        
        for word in strs:
            new_dic = {}
            
            for letter in word:
                if letter in new_dic:
                    new_dic[letter] += 1
                else:
                    new_dic[letter] = 1
            
            for i, dic in enumerate(dics):
                if new_dic == dic:
                    res[i].append(word)
                    break
            else:
                dics.append(new_dic.copy())
                res.append([word])
        return res