class Solution:
    def maximumSwap(self, num: int) -> int:
        heap = []
        str_num = str(num)
        for digit in str_num:
            heapq.heappush(heap, -int(digit))
        
        for i, digit in enumerate(str_num):
            if -int(digit) == heap[0]:
                heapq.heappop(heap)
            else:
                min_val = None
                min_ind = None

                for j in range(i+1, len(str_num)):
                    mdigit = int(str_num[j])

                    if min_val is None or mdigit >= min_val:
                        min_val = mdigit
                        min_ind = j
                if min_val is None:
                    return num

                n_lst = list(str_num)
                print(n_lst, min_ind)
                n_lst[i], n_lst[min_ind] = str(n_lst[min_ind]), str(n_lst[i])
                return int(''.join(n_lst))
        return num
