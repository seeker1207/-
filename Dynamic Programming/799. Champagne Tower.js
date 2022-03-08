/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
/*
    샴페인 한잔을 따를때마다 어떻게 변하는지 추적하지않고,
    총 따를 잔수를 맨위에서 더한뒤 그뒤의 잔들을 계산해주면서 내려가면 쉽게 풀이 가능.
*/
var champagneTower = function(poured, query_row, query_glass) {
    const dp = Array(101).fill(null).map(() => Array(101).fill(0));
        
    dp[0][0] = poured;
    
    for (let j = 0; j < query_row + 1; j++) {
        for (let k = 0; k < j + 1; k++) {
            let down = (dp[j][k] - 1) / 2;
            
            if (down > 0) {
                dp[j + 1][k] += down;
                dp[j + 1][k + 1] += down;
            }
        }
    }

    return Math.min(1, dp[query_row][query_glass]);
};
