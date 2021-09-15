/**
 * 문자열중 오직 영어문자만 리버스 시키는 문제인데 나는 투포인터로 풀었지만 스택으로 훨씬 쉽게 풀수 있다.
 * 문자열에서 영어문자로만 이루어진 새로운 문자열을 생성하고 원래 문자열을 돌면서 영어 문자열이 아닌 경우 그대로 append 하고 아니라면 새로운 문자열에서 pop해서 append 하면 
 * 오직 영어문자만 리버스 시킬 수 있다.
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    let [left, right] = [0, s.length - 1];
    let sArray = s.split('');
    
    while (left <= right) {
        while (!/[a-zA-Z]/.test(sArray[left])) left++;
        while (!/[a-zA-Z]/.test(sArray[right])) right--;
        
        if (left > right) break;
        
        if (/[a-zA-Z]/.test(sArray[left]) && /[a-zA-Z]/.test(sArray[right])) {
            // console.log(sArray, left,right, 'in')
            let temp = sArray[left];
            sArray[left] = sArray[right];
            sArray[right] = temp;
        }

        left++;
        right--;
    }
    
    return sArray.join('');
};
