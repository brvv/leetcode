class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        checked_cities = set({})
        provinces = 0

        for city_num, city_connections in enumerate(isConnected):
            if city_num not in checked_cities:
                provinces += 1
                checked_cities.add(city_num)
                stack = [city_num]
                
                while stack:
                    current_city = stack.pop()
                    connections = []

                    #find connections
                    for other_i, other_city in enumerate(isConnected[current_city]):
                        if other_city == 1 and other_i not in checked_cities:
                            checked_cities.add(other_i)
                            connections.append(other_i)

                    stack += connections.copy()
        return provinces



'''
[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]
'''