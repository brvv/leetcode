class Solution:
    def isSubstring(self, pstring, sub):
        for key in sub:
            if key in pstring and pstring[key] >= sub[key]:
                continue
            else:
                return False
        return True

    def getDict(self, s):
        res = {}
        for letter in s:
            if letter in res:
                res[letter] += 1
            else:
                res[letter] = 1
        return res
    
    def mergeStrings(self, target, mergee):
        print(target, mergee)
        for key in mergee:
            if key not in target:
                target[key] = mergee[key]
            else:
                target[key] = max(target[key], mergee[key])
        return target


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words1dicts = [self.getDict(word) for word in words1]
        words2dicts = [self.getDict(word) for word in words2]

        reduce(lambda target, mergee : self.mergeStrings(target, mergee), words2dicts)
        unistring = words2dicts[0]

        res = []

        for i, wordDict in enumerate(words1dicts):
            if self.isSubstring(wordDict, unistring):
                res.append(words1[i])
        return res