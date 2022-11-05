class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        lst_sum = sum(nums)
        
        if lst_sum % 2 != 0:
            return False
        
        target = lst_sum // 2
        
        def subsetSumTokRow(arr, target):
            row = [False for i in range(target + 1)]

            #first row of table
            row[0] = True
            if arr[0] < len(row):
                row[arr[0]] = True

            for row_i in range(0, len(arr)-1):
                new_row = [False for i in range(target + 1)] 
                for col_i in range(0, len(row)):
                    item = row[col_i]

                    if item:
                        #dont include next val
                        new_row[col_i] = True
                        #include next val
                        if arr[row_i+1] + col_i < len(new_row):
                            new_row[col_i + arr[row_i+1]] = True
                row = new_row
            return row[-1]
        
        return subsetSumTokRow(nums, target)