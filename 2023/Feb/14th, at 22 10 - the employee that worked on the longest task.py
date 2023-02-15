class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        employee = logs[0][0]
        time = logs[0][1]

        for i in range(1, len(logs)):
            task_time = logs[i][1] - logs[i-1][1]
            if task_time > time:
                time = task_time
                employee = logs[i][0]
            elif task_time == time:
                employee = min(logs[i][0], employee)
        return employee