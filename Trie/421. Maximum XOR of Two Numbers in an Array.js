/**
 * @param {number[]} nums
 * @return {number}
 */

/*
    trie 구조에 num 의 이진수의 비트 하나하나를 넣는다.
    각 num마다 최대값 (111....) 이 될수 있는 나머지 하나의 수를 찾는다. (two sum 과 비슷)
    
    각 비트 자리수를 순회한다.
    
    1. 결과값이 1이 나올 수 있는 num이 있다면, (trie 구조에 해당 비트가 있다면,)
        결과값에 그 자릿수를 더한다. 
    2. 결과값이 1이 나올 수 있는 num이 없다면, (trie구조에 해당 비트가 없다면,)
        반대 비트에 해당하는 trie 구조로 계속 탐색한다.
    
    각 num 마다 나올수 있는 최대값을 찾고, 그 최대값중에 가장 큰값을 리턴.
     
*/
var findMaximumXOR = function(nums) {
    const trie = new Map();
    let result = 0;
    
    for (let num of nums) {
        let cur = trie;
        
        for (let i=31; i--; i >= 0) {
            const bit = (num >> i) & 1;

            if (!cur.has(bit)) {
                cur.set(bit, new Map());  
            }
            cur = cur.get(bit);
        }    
    }
    
    
    for (let num of nums) {
        let cur = trie;
        let numMax = 0;    
        for (let i = 31; i--; i>= 0) {
            const targetBit = 1 - ((num >> i) & 1);
            
            if (cur.has(targetBit)) {
                numMax += 1 << i;
                cur = cur.get(targetBit);
            } else {
                cur = cur.get(1 - targetBit);
            }
        }
        
        result = Math.max(numMax, result);
    }
    
    return result;
};
