# the definition of an Eulerian trail (a path that traverses every edge exactly once).
# Instead of trying to prepend or insert segments later, the algorithm appends nodes after we have exhausted all outgoing edges from that node. This creates the path in reverse order. Final reversal gives the correct itinerary.


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # Sorting the tickets in reverse order so we can pop from the end (O(1))
        for source, destination in sorted(tickets, reverse=True):
            graph[source].append(destination)
        
        print(f"{graph=}")
        res = []
        
        def dfs(node):
            # While there are available destinations from this source
            while graph[node]:
                # Remove the lexicographically smallest available destination
                next_dest = graph[node].pop()
                dfs(next_dest)
            # Post-order traversal: add to result after exploring all paths
            res.append(node)
            
        dfs("JFK")
        # The path is found in reverse order
        return res[::-1]