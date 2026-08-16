class Solution:
    def dfs(self, i, adj_matrix, visited):
        visited[i] = True
        for x in range(len(adj_matrix)):
            if adj_matrix[i][x] == 1 and not visited[x]:
                self.dfs(x, adj_matrix, visited)

            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                count += 1

        return count
