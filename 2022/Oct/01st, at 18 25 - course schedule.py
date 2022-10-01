class Solution:
    def __init__(self):
        self.canComplete = {}
    
    
    def dfs(self, dic, courseNum, preSet=set([])):
        if courseNum not in dic or courseNum in self.canComplete:
            self.canComplete[courseNum] = True
            return True
        
        prerequisites = dic[courseNum]
        
        
        
        for prereq in prerequisites:
            if prereq in preSet:
                return False
            else:
                if (not self.dfs(dic, prereq, preSet.union([courseNum]))):
                    return False
                
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        
        for [course, prereq]  in prerequisites:
            dic[course].append(prereq)
            
        
        for course in range(numCourses):
            if(self.dfs(dic, course)):
                self.canComplete[course] = True
                continue
            else:
                return False
            
    
        return True