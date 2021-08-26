/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length < 1){
        return [];        
    }
    let output = [];
    const phoneStr = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    const getCombi = (digitsIdx, candi) => {
        
        if (digitsIdx > digits.length - 1) {
            output.push(candi);  
            return;
        }
        
        phoneStr[digits[digitsIdx]].split('').forEach((char) => {
            candi += char;
            getCombi(digitsIdx + 1, candi);
            candi = candi.slice(0, candi.length - 1);
        })
          
    }
    
    getCombi(0, []);
    
    return output;
};
