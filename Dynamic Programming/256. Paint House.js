/**
 * @param {number[][]} costs
 * @return {number}
*/
/*
  dp로 풀면 간단하다. 매번 3가지 색상에 대한 최적의 값을 찾아서 순회한다. 
  ...ex) 빨간색으로 칠해진 경우의 최소값 = (그 이전의 파랑 노랑으로 칠해진 경우 중 작은값 + 현재 빨간색으로 칠했을때의 cost)
*/
var minCost = function(costs) {
    const dp = new Array(3).fill(null).map(() => new Array(costs.length).fill(-1));
    const n = costs.length;
    
    dp[0][0] = costs[0][0];
    dp[1][0] = costs[0][1];
    dp[2][0] = costs[0][2];
    
    // console.log(dp)
    for (let j=1; j<n; j++) {
        dp[0][j] = Math.min(dp[1][j - 1] + costs[j][0], dp[2][j - 1] + costs[j][0]);
        dp[1][j] = Math.min(dp[0][j - 1] + costs[j][1], dp[2][j - 1] + costs[j][1]);
        dp[2][j] = Math.min(dp[0][j - 1] + costs[j][2], dp[1][j - 1] + costs[j][2]);
    }
    
    return Math.min(dp[0][n-1], dp[1][n-1], dp[2][n-1]);
};
