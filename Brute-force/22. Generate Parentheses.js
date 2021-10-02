/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let parens = []
    let result = [];
    
    let isValid = (paren) => {
        let q = [];
        for (let str of paren) {
            if (str == '(') q.push(str);
            else {
                if (q.length == 0) return false;
                q.pop()
            }
        }
        
        return q.length == 0;
    }
    
    let getParen = (cnt) => {
        if (cnt == n*2) {
            if (isValid(parens)) {
                result.push(parens.slice(0).join(''))    
            }
            
            return;
        }
    
        for (let p of ['(', ')']) {
            parens.push(p);
            getParen(cnt + 1)
            parens.pop();
        }
    }
    
    getParen(0);
    return result;
};
