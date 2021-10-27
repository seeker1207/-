/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let cntList = new Array(3).fill(0);
    let result = [];
    
    for (let num of nums) {
        cntList[num]++;
    }
    
    let idx = 0;
    
    cntList.forEach((cnt, color) => {
        while(cnt-- > 0) nums[idx++] = color;
    })
    
    return nums;
    
};
