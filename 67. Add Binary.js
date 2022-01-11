/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let result = '';
    let carry = 0;
    
    let idxA = a.length - 1;
    let idxB = b.length - 1;
    
    let sum = 0;
    while (idxA >= 0 || idxB >= 0) {
        sum = carry;
        
        if (idxA >= 0) sum += +a[idxA--];
        if (idxB >= 0) sum += +b[idxB--];
        
        carry = sum > 1? 1 : 0;
        
        result = `${sum%2}${result}`;
        // result.push(sum % 2);
        
    }
    
    // if (carry != 0) result.push(carry);
    
    return carry != 0 ? `${carry}${result}` : result;
};
