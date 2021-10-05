/**
 * @param {number[][]} dungeon
 * @return {number}
 */
var calculateMinimumHP = function(dungeon) {
    let [N, M] = [dungeon.length, dungeon[0].length];
    let dp = new Array(N + 1).fill(null).map(() => new Array(M + 1).fill(Number.MAX_SAFE_INTEGER));
    
    dp[N][M-1] = 1;
    dp[N-1][M] = 1;
    
    for (let n = N - 1; n >= 0; n--) {
        for (let m = M - 1; m >= 0; m--) {
            dp[n][m] = Math.max(1, Math.min(dp[n+1][m], dp[n][m+1]) - dungeon[n][m])
        }
    }
    
    return dp[0][0]
};
