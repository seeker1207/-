function solution(n, s, a, b, fares) {
    var answer = 0;
    const graph = {};
    let dp = new Array(n+1).fill(new Array(n+1).fill(Infinity));
    // console.log(dp)
    for (let i=0; i<n+1; i++) {
        dp[i][i] = 0;
    }
    
    fares.forEach((fr) => {
        const [start, end, fare] = fr;
        dp[start][end] = fare;
        dp[end][start] = fare;
    })
    
    console.log(dp)
    
    
    return answer;
}
