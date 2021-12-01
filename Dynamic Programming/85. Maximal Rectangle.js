/**
 * @param {character[][]} matrix
 * @return {number}
 */

/*
    각 row마다 matrix[i][j]에서 시작될수 있는 최대 1의 컬럼 길이를 미리 dp로 구한다.
    각 cell 마다 row를 끝까지 순회하면서 그 중 
    가장 작은 가로길이(최대 1의 컬럼 길이 중 가장 작은 길이)를 구하고 
    세로길이 (row - i + 1) 와 곱해 최대값을 업데이트 한다.

*/
var maximalRectangle = function(matrix) {
    if (!matrix.length) return 0;
    let ret = 0;
    const [R, C] = [matrix.length, matrix[0].length];
    const dp = new Array(R + 1).fill(null).map(() => new Array(C + 1).fill(0));
    console.log(R, C)
    for (let i = R - 1; ~i; i--) {
        for (let j = C - 1; ~j; j--) {
            dp[i][j] = matrix[i][j] == '1' ? dp[i][j + 1] + 1 : 0;
        }
    }
    
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            let minLen = C;
            for (let row = i; row < R && matrix[row][j] === '1'; row++) {
                minLen = Math.min(minLen, dp[row][j]);
                ret = Math.max(ret, (row - i + 1) * minLen);
            }
        }
    }
    
    return ret;    
};
