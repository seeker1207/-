/**
 * @param {number[]} nums
 * @return {number}
 */
/*
  dp의 풀이의 경우 배열이 + 방향으로 끝났을떄, - 방향으로 끝났을떄의 최대값들을 이전 최대값을 이용해 구해가면서 마지막 최종값을 구하면 된다.
  
  그리디 풀이의 경우 이전의 변화의 방향 (preDiff)을 계속 유지해가면서 현재의 변화의 방향과 다르면 count에 +를 해준다. 
  이때 변화가 없을경우(prevDiff = 0)를 유의해서 처리해줘야한다.
  변화가 없다면 방향은 변하지 않은 상태이다. 
*/
var wiggleMaxLength = function(nums) {
//     let dp = Array(2).fill(null).map(() => Array(nums.length).fill(-1));
//     dp[0][0] = 1;
//     dp[1][0] = 1;
    
//     // dp[0] +, dp[1] -
//     for (let i=1; i<nums.length; i++) {
//         if (nums[i - 1] < nums[i]) {
//             dp[0][i] = dp[0][i-1];
//             dp[1][i] = Math.max(dp[0][i-1] + 1, dp[1][i-1]);
//         } else if (nums[i - 1] > nums[i]) {
//             dp[0][i] = Math.max(dp[1][i-1] + 1, dp[0][i-1]);
//             dp[1][i] = dp[1][i-1];
//         } else {
//             dp[0][i] = dp[0][i-1];
//             dp[1][i] = dp[1][i-1];
//         }
//     }
    
//     return Math.max(dp[0][nums.length - 1], dp[1][nums.length - 1]);
    
    if (nums.length < 2)
        return nums.length;
    
    let prevDiff = nums[1] - nums[0];
    let count = prevDiff !== 0? 2: 1;
    
    for (let i=2; i<nums.length; i++) {
        const diff = nums[i] - nums[i - 1];
        if ((diff < 0 && prevDiff >= 0 ) || (diff > 0 && prevDiff <= 0)) {
            count++;
            prevDiff = diff;
        }
        
        // console.log(prevDiff, count)
    }
    
    return count;
};
