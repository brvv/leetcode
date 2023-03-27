class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        queue = deque(customers)

        curr_time = 0
        time_sums = 0

        while len(queue)>0:
            order_time, prep_time = queue.popleft()
            curr_time = max(order_time, curr_time) + prep_time
            wait_time = curr_time - order_time
            time_sums += curr_time - order_time

        return time_sums / len(customers)

