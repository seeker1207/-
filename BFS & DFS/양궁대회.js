/*
  10점부터 피치보다 한발을 더 쏴서 점수를 얻는경우, 한발도 쏘지않는 경우 2가지가 있다.
  따라서 각 2가지 경우로 분기를 태워 dfs 탐색을 한다.
  최악의경우면 2^10 정도의 시간복잡도이므로 통과가 가능하다.
  
  쏴야할 화살 갯수가 넘는 경우 return 한다. (백트래킹)
  0점 까지 갔는데 쏴야할 화살 갯수가 남은경우 0점에 다 맞춘걸로 판단 한다. 
  (어차피 가장 낮은 점수를 많이 맞춘 쪽을 반환해야하므로)
*/

function solution(n, info) {
    var answer = Array(11).fill(0);
    let maxDiff = 0;
    
    const compare = (a, b) => {
        for (let i = a.length; i >= 0; i--) {
            if (a[i] > b[i]) return a;
            else if (a[i] < b[i]) return b;
        }
        
        return a;
    }
    
    const getDiff = (arr) => {
        let [apSum, lionSum] = [0, 0];
        
        for (let i = 0; i < 10; i++) {
            if (arr[i] === 0 && info[i] === 0 ) continue;
            if (arr[i] <= info[i]) apSum += 10 - i;
            else lionSum += 10 - i;
        }
        
        return lionSum - apSum;
    };
    
    const getScore = (arrowCnt, curArr, scoreIdx) => {
        if (arrowCnt > n) {
            return;
        }
        if (scoreIdx > 10) {
            curArr[10] += n - arrowCnt;
            const diff = getDiff(curArr);
            if (diff > maxDiff) {
                maxDiff = diff;
                answer = curArr;
            } else if (diff === maxDiff) {
                answer = compare(curArr, answer);
            }
            return;
        }
        
        const targetCnt = info[scoreIdx] + 1;
        
        getScore(arrowCnt, [...curArr, 0], scoreIdx + 1);
        getScore(arrowCnt + targetCnt, [...curArr, targetCnt], scoreIdx + 1);
        
    };
    
    getScore(0, [], 0);

    return maxDiff === 0 ? [-1]: answer;
}
