/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let dp = new Array(nums.length).fill(10001);

    const getJump = (ps) => {
        if (dp[ps] !== 10001) return dp[ps];
        
        if (ps === nums.length - 1) return 0;
        
        for (let i = 1; i < nums[ps] + 1; i++) {
            if (ps + i > nums.length - 1) continue;
            dp[ps] = Math.min(dp[ps], 1 + getJump(ps + i));
        }
        
        return dp[ps];
    }
   
    return  getJump(0);
};
