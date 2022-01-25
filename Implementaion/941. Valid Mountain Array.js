/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    let valey = false;
    let pre = -1;
    
    if (arr[0] > arr[1]) return false;
    
    for (let h of arr) {
        if (pre === h) return false;
        
        if (!valey && pre > h) {
            valey = true;
        }
        
        if (valey && pre < h) {
            return false;
        }
        pre = h;
    }
    
    if (!valey) return false;
    return true;
};
