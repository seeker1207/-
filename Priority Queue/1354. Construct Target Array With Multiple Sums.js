/**
 * @param {number[]} target
 * @return {boolean}
 */
/*
  지금 현재 타겟 배열이 나오게된 이전 배열을 생각하면 보다 수월하게 풀수 있다.
  타겟 배열에서 가장 큰수가 이전 배열의 합을 의미한다.
  따라서 (현재 배열의 합 - 현재 배열의 가장 큰 수)를 하면 이전 배열에서 교체된 원소가 무엇인지 알수 있다.
  
  [9, 3, 5] => [1, 3, 5] 여기서 9를 1로 교체할수 있음을 알수 있다. 9 => (9 - (5+3))
  이런식으로 반복하여 [1, 1, 1]이 나오게끔 하면된다.
  
  여기서 [2, 535] 이런 방식의 배열이 문제가 될수 있는데, 이런 경우를 대비하여 '마이너스' 대신 '나머지 연산' 으로 하면 시간을 더 많이 줄일 수 있다.
  (2, 533) => (2, 531) => ....   (2, 533 % 2)
  
*/
var isPossible = function(target) {
    
    if (target.length === 1) return target[0] === 1;
    
    
    const pq = new MaxPriorityQueue();
    target.forEach((num) => pq.enqueue(num))
    
    let sum = target.reduce((prev, curr) => prev + curr, 0);
    // console.log(pq.front())
    while (pq.front().element > 1) {
        const maxNum = pq.dequeue().element;
        const sumWithoutMax = sum - maxNum;
        
        console.log(target, sum, maxNum, sumWithoutMax)
       // 나누는 수가 1이 되는 경우는 무조건 나머지가 0이 되므로 주의해야 한다.
       // 큰수를 뺸 나머지 합이 1이 되는 경우는 원소 1만 남았을경우 이므로 n=2인경우라는 것을 알수 있다. 이는 결국 (1,1)이 남으므로 더 계산할 필요없이 true로 리턴한다.
        if (sumWithoutMax === 1) {
            return true;
        }
        
        const nextNewNum = maxNum % sumWithoutMax;
        
        if (nextNewNum === 0 || nextNewNum === maxNum) return false;
        
        pq.enqueue(nextNewNum);
        
        sum = sum - maxNum + nextNewNum;
        
    }
    
    return true;
};
