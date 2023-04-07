class Solution {
    private final int[] dirX = {0, 1, 0, -1};
    private final int[] dirY = {-1, 0, 1, 0};

    public void dfs(int x, int y, int m, int n, int[][] grid, boolean[][] visited) {
    if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0 || visited[x][y]) {
        return;
    }

    visited[x][y] = true;

    for (int i = 0; i < 4; i++) {
        dfs(x + dirX[i], y + dirY[i], m, n, grid, visited);
    }

    return;
}
    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1 && !visited[i][0]) {
                dfs(i, 0, m, n, grid, visited);
            }
            if (grid[i][n - 1] == 1 && !visited[i][n - 1]) {
                dfs(i, n - 1, m, n, grid, visited);
            }
        }

        for (int i = 0; i < n; i++) {
            if (grid[0][i] == 1 && !visited[0][i]) {
                dfs(0, i, m, n, grid, visited);
            }
            if (grid[m - 1][i] == 1 && !visited[m - 1][i]) {
                dfs(m - 1, i, m, n, grid, visited);
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    count++;
                }
            }
        }
        return count;
    }
}
