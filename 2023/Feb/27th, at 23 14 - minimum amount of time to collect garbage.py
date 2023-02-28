class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        counts = {}
        counts['G'] = 0
        counts['P'] = 0
        counts['M'] = 0
        last_occurences = {}

        driving_time = 0

        for i, house in enumerate(garbage):
            for item in house:
                counts[item] += 1
                last_occurences[item] = i
        
        for gtype in ['G', 'P', 'M']:
            if gtype in last_occurences:
                driving_time += sum(travel[0:last_occurences[gtype]])
                driving_time += counts[gtype]

        return driving_time