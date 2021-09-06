function solution(n, s, a, b, fares) {
    var answer = Infinity;
    const graph = {};
    let dp = new Array(n).fill(null).map(() => 
            new Array(n).fill(null).map(() => Infinity));
 
    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            if (i == j) {dp[i][i] = 0;}
        }
    }

    fares.forEach((fr) => {
        const [start, end, fare] = fr;
        dp[start-1][end-1] = fare;
        dp[end-1][start-1] = fare;
    })


    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            for (let k=0; k<n; k++) {
                dp[j][k] = Math.min(dp[j][k], dp[j][i] + dp[i][k])
            }
        }
    }
    
    for (let l=0; l<n; l++) {
        answer = Math.min(answer, dp[s-1][l] + dp[l][a-1] + dp[l][b-1]);
    }
    
    return answer;
}
