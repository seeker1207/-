/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let numHash = new Map();
    let resultSet = new Set();
    
    if (nums.length <= 2) {
        return []
    }
    nums.forEach((num, idx) => {
        if (numHash.has(num)) numHash.get(num).push(idx);
        else numHash.set(num, [idx]);
    })
    
    
    for (let i=0; i<nums.length; i++) {
        const target = -nums[i];
        for (let j=0; j<nums.length; j++) {
            const third = numHash.get(target - nums[j]);
            if (third) {
                const candidate = [nums[i], nums[j], target - nums[j]];
                if (resultSet.has(candidate.sort((a,b) => a-b).join(' '))) continue;

                for (let thirdIdx of third) {
                    if (i !== j && j !== thirdIdx && i !== thirdIdx) {
                        resultSet.add(candidate.sort((a, b) => a-b).join(' '));
                    }
                }
            }

        }
    }
    
    let result = []
    resultSet.forEach((elm) => {
        result.push(elm.split(' '))
    })
    
    return result
};
