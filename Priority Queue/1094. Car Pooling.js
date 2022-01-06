/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
/*
  우선순위 큐를 이용하면 더 빠른시간복잡도를 가질수 있지만, 
  자바스크립트의 경우 구현된 기본 모듈이 없어 for문으로 대신함.
  
  승객 탑승시작시간으로 정렬된 trips 리스트를 순회하면서 각각의 end 시점(승객이 내리는 지점)을 미리 hash로 기록하고,
  현재 start 지점과 비교하여 hash에 있는 끝난 시점의 모든 trip들을 다 정리한다.
  
  그래서 마지막에 계산된 cur(현재 Capicity)가 기준 capacity보다 크면 더 많은 좌석이 필요하므로 false.
  -------------
  
  우선순위 큐를 쓰지않고 모두 trip의 capicity를 리스트에 미리 저장하는 방법도 있다.
  구간을 생각하지 않고 승객 탑승 시점의 승객수를 해당 인덱스에 + 하고 내리는 시점의 내린승객수를 -한뒤
  리스트의 값들을 기준 capicity에 모두 다 빼본뒤 0보다 작으면 False.
*/
var carPooling = function(trips, capacity) {
    const hash = new Map();
    trips.sort((a, b) => a[1] - b[1]);
    let cur = 0;
    
    for (let [cp, start, end] of trips) {
        cur += cp;
        
        for (let [stop, stopCp] of hash) {
            if (stop <= start) {
                cur -= stopCp;
                hash.delete(stop);
            }
        }
        
        if (cur > capacity) return false;
        
        hash.set(end, (hash.get(end) || 0) + cp);
    }
    
    return true;
    
};
