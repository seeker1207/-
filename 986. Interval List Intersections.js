/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
/*
    두 리스트의 인터벌 중에 가장 작은 엔드포인트를 찾는다.
    그 엔드 포인트가 A[0]의 엔드포인트라면 A[0] 은 B[0]에만 교집합이 있을수 있다.
    왜냐하면 A[0]이 B 리스트의 두개의 인터벌과 교집합이 있다면 
    같은 엔드포인트를 공유하고 있다는 이야기인데,
    이건 각 인터벌들이 서로 서로소라는 가정에 모순된다.
    따라서 A[0]은 B[0]에만 매칭될수 있으므로 서로 교집합이 있는지 확인한후, 
    체크대상에서 제외시킬수 있다.

*/
var intervalIntersection = function(firstList, secondList) {
    let result = [];
    let [i, j] = [0, 0];
    
    while (i < firstList.length && j < secondList.length) {
        
        // 두 구간의 교집합이 있는지 확인
        let maxSt = Math.max(firstList[i][0], secondList[j][0]);
        let minEd = Math.min(firstList[i][1], secondList[j][1]);
        
        if (maxSt <= minEd) result.push([maxSt, minEd]);
        
        if (firstList[i][1] < secondList[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    
    return result;
};
