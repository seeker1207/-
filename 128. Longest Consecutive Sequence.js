/**
 * @param {number[]} nums
 * @return {number}
 */
/*
    연속된 배열의 최대 길이를 구해야한다.
    
    1. 전체 배열을 세트 구조에 넣는다.
    2. 배열을 다시 순회하면서 현재 숫자 - 1 에 해당하는 숫자가 세트에 있는지 확인한다.
    3. 숫자 - 1 이 있으면 그 숫자는 전체 연속된 배열의 시작점이 아니다.
    4. 숫자 - 1 이 없으면 그 숫자는 연속된 배열의 시작점이므로 
        그 숫자부터 연속된 배열의 길이가 어느정도되는지 구한다.
    
*/
var longestConsecutive = function(nums) {
   
    let numSet = new Set(nums);
    let maxLength = 0;
    
    for (let num of nums) {
        if (!numSet.has(num - 1)) {
            let tempNum = num;
            let tempLength = 1;
            while (numSet.has(tempNum + 1)) {
                tempNum += 1;
                tempLength += 1;
            }
            
            maxLength = Math.max(tempLength, maxLength);
        }
    }
    
    return maxLength;
};
