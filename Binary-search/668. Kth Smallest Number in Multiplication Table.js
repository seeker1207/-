/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
/*
    k 번째로 작은 숫자를 찾는 문제.
    m * n 을 다 돈다면 시간 초과가 나므로 이진탐색을 이용하여 푼다.
    k는 결국 [1 ... m*n] 사이에 있다.
    따라서 그 사이의 숫자중 임의의 숫자를 x라고 하면 
    테이블에서 x보다 작거나 같은 수가 몇 개나 있는지 찾고,
    
    1) 만약 그 수가 k보다 크거나 같다면 k번째 수가 1 ~ x까지의 숫자 안에 있을만큼 충분하므로
       1 ~ x 안에 k번째 수가 있다.
    
    2) 그 수가 k보다 작으면 (x + 1) ~ (m * n) 안에 k번째 수가 있다.
    
    그런식으로 탐색범위를 줄여나가서 k번째 수를 찾는다.
*/
var findKthNumber = function(m, n, k) {
    
    const enough = (x) => {
        let count = 0;
        for (let i = 1; i <= m; i++) {
            count += Math.min(Math.floor(x / i), n);
        }
        return count >= k;
    }
    
    let [lo, hi] = [1, m*n];
    
    while (lo < hi) {
        let x = Math.floor((lo + hi) / 2);
        if (!enough(x)) {
            lo = x + 1;
        } else {
            hi = x;
        }
        
    }
    
    return lo;
};
