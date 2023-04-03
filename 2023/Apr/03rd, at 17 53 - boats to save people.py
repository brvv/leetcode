class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s_people = sorted(people, reverse=True)

        max_heap = []

        boats = 0

        for person in s_people:
            if len(max_heap) > 0 and -max_heap[0] >= person:
                space = -heappop(max_heap)
            else:
                boats += 1
                space = - (limit - person)
                if space < 0:
                    heappush(max_heap, space)
        return boats


    
# sort people
# start with largest
# put a person to boat, add remaining space to max heap
# on next person, check if enough space on max heap
#   if not, add another boat
#   if enough, pop boat, change space, add to max heap
#  