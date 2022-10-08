class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for word in strs:
            letters = [0 for i in range(26)]
            offset = ord('a')
            
            for letter in word:
                letters[ord(letter) - offset] += 1
            
            dic[tuple(letters)].append(word)
            
        return dic.values()
            