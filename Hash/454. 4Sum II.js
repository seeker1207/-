/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
/*
    1. nums1 과 nums2의 각 숫자들의 합을 미리 해쉬구조에 저장 해놓는다.
    
    2. nums3 와 nums4의 각 숫자들의 합을 구하면서,
    합이 0이 되게하는 값을 미리세어준 합에서 찾아 
    최종 결과 카운트에 합해준다.

*/
var fourSumCount = function(nums1, nums2, nums3, nums4) {
    const sumHash = {};
    let tupleCnt = 0;
    
    for (let num1 of nums1) {
        for (let num2 of nums2) {
            const sum = num1 + num2;
            if (sum in sumHash) {
                sumHash[sum] += 1;
            } else {
                sumHash[sum] = 1;
            }
        }
    }
    
    for (let num3 of nums3) {
        for (let num4 of nums4) {
            const target = -(num3 + num4);
            if (target in sumHash) {
                tupleCnt += sumHash[target];
            }
        }
    }
    
    
    return tupleCnt;
};
