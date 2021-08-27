/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let [left, right] = [0, nums.length - 1];
    let targetPoint = null;
    let [targetLeft, targetRight] = [0, 0];
    
    if (nums.length === 1) {
        if (target === nums[0]) return [0, 0]
        else return [-1, -1]
    }
    // console.log(left, right, targetPoint, targetLeft, targetRight)
    // console.log(left+right /2)
    while(left <= right) {
        middle = parseInt((left + right) / 2);
        
        if (nums[middle] > target) right = middle - 1;
        else if (nums[middle] < target) left = middle + 1;
        else {
            targetPoint = middle;
            break;
        }
    }
    
    
    if (targetPoint !== null) {
        let temp = targetPoint;
        while (nums[++temp] === target);
        targetRight = temp - 1;
            
        temp = targetPoint
        while (nums[--temp] === target); 
        targetLeft = temp + 1;
        
    } else {
        [targetRight, targetLeft] = [-1, -1]
    }
    
    return [targetLeft, targetRight];
};

