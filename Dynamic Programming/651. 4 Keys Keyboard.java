class Solution {
    /**
    1. ...(m번 이라고가정), Ctrl+A, Ctrl+C, Ctrl+V 를 누른다면 m + 3번이므로
    처음 길이를 l 이라고 할때 2l 이 되기위한 최소한의 수는 m + 3번이다.
    2. 거기서 한번더 Ctrl+V 누르면 3l이 된다.
    3. 이런식으로 dp[i + 6] = 5 * dp[i] 이라고 할수 있다.
    4. 그 이상은 의미가 없는것이
    Ctrl+A, Ctrl+C, Ctrl+V, Ctrl+A, Ctrl+C, Ctrl+V, Ctrl+V (m + 7)를 한다고 했을때 6l이  되는데, 4번쨰에 전체를 선택하고 복사를 할때 이미 2l 이 들어있으므로 이는 앞서 말한 경우(m + 3)에 포함이 된다.
    5. 따라서, dp[j] = (j - i = 1) * dp[i] (i + 3 <= j <= i + 6) 이다.
     */ 
    public int maxA(int n) {
        int[] dp = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            dp[i] = i;
        }

        for (int i = 0; i <= n - 3; i++) {
            for (int j = i + 3; j <= Math.min(n, i + 6); j++) {
                dp[j] = Math.max(dp[j], (j - i - 1) * dp[i]);
            }
        }

        return dp[n];
    }
}
