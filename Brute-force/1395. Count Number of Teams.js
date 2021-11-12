/**
 * @param {number[]} rating
 * @return {number}
 */

/*
    rating의 모든 값을 반복하면서 해당 값을 중앙값으로 두고,
    왼쪽과 오른쪽 값중에 작거나 큰값을 카운트 한다.
    그러고 나서,
    (왼쪽 작은값 * 오른쪽 큰값) + (왼쪽 큰값 * 오른쪽 작은값)을 구하면
    그 중앙값을 기준으로한 경우의 수를 구할수 있다.
*/
var numTeams = function(rating) {
    let N = rating.length;    
    let res = 0;
    
    for (let i = 0; i < N; i++) {
        let [lsLeft, gtRight, lsRight, gtLeft] = [0, 0, 0, 0];
        
        for (let j = 0; j < N; j++) {
            if (j < i && rating[j] < rating[i]) lsLeft++
            if (j > i && rating[j] > rating[i]) gtRight++
            if (j > i && rating[j] < rating[i]) lsRight++
            if (j < i && rating[j] > rating[i]) gtLeft++
        }
        
        res += (lsLeft * gtRight) + (gtLeft * lsRight);
    }
    
    return res;
};
