class Solution:
    def mergeDicts(self, dict1, dict2):
        #26 letters, so this is constant time
        res = {}

        for key in dict1:
            res[key] = dict1[key]

        for key in dict2:
            if key in res:
                res[key] += dict2[key]
            else:
                res[key] = dict2[key]
        return res

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        connections = defaultdict(list)
        checked_nodes = set({})
        res = [0 for i in labels]

        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

        def countNodesRec(edges, labels, curr_node = 0):
            checked_nodes.add(curr_node)
            

            if curr_node not in connections:
                label = {}
                label[labels[curr_node]] = 1
                res[curr_node] = 1
                return label

            curr_letter = labels[curr_node]
            curr_labels = {}
            curr_labels[curr_letter] = 1

            for child_node in connections[curr_node]:
                if child_node in checked_nodes:
                    continue
                child_label = countNodesRec(edges, labels, child_node)

                curr_labels = self.mergeDicts(curr_labels, child_label)

            res[curr_node] = curr_labels[curr_letter]
            return curr_labels

        countNodesRec(edges, labels)
        return res
            

