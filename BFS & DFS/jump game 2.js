/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    let q = [start];
    let nowIdx = null;
    let visited = new Set();
    let isReach = false;
    
    while (q.length > 0) {
        nowIdx = q.shift();
        
        if (arr[nowIdx] === 0) {
            isReach = true;
            break;
        }
        
        let [left, right] = [nowIdx - arr[nowIdx], nowIdx + arr[nowIdx]];
        
        if (!visited.has(right) && nowIdx + arr[nowIdx] < arr.length){
            visited.add(right);
            q.push(nowIdx + arr[nowIdx]);
            
        }
        if (!visited.has(left) && nowIdx - arr[nowIdx] >= 0) {
            visited.add(left);
            q.push(nowIdx - arr[nowIdx]);
        }
        
    }
    
    return isReach;
};
