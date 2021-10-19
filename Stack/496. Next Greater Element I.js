/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let cache = new Array(10000).fill(null);
    
    nums2.forEach((num, idx)  => cache[num] = idx);
    
    let result = nums1.reduce((pre, num) => {
        let fstBigger = -1;
        for (let i=cache[num] + 1; i<nums2.length; i++) {
            if (nums2[i] > num) {
                fstBigger = nums2[i];
                break;
            }
        }
        pre.push(fstBigger);
        return pre;
    }, [])
    
    return result
};
