87. Scramble String

class Solution {
    // 이전에 계산된 substring의 부울값을 저장한다. (서로 scrambled 된 문자열인지?)
    Map<String, Boolean> map = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        int n = s1.length();

        // 두 문자열이 같은지 체크한다.
        if (s1.equals(s2)) {
            return true;
        }    

        // s1, s2, s2의 자르고난 후 오른쪽 문자열의 문자 빈도수가 저장된 배열을 초기화한다. 
        int[] a = new int[26], b = new int[26], c = new int[26];

        if (map.containsKey(s1 + s2)) {
            return map.get(s1 + s2);
        }

        for (int i = 1; i <= n - 1; i++) {
            int j = n - i;

            // s1, s2, 현재 substring의 빈도수를 저장한다.
            a[s1.charAt(i - 1) - 'a']++;
            b[s2.charAt(i - 1) - 'a']++;
            c[s2.charAt(j) - 'a']++;

            // 현재 substring과 같은 문자들을 갖고 있는지 체크한다.
            if (Arrays.equals(a, b) && isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) {
                // if the substrings are scrambled versions of each other, return true
                map.put(s1 + s2, true);
                return true;
            }
            // 현재 substring과 s2의 오른쪽 문자열의 문자 빈도수가 같은지 체크한다.
            if (Arrays.equals(a, c) && isScramble(s1.substring(0, i), s2.substring(j)) && isScramble(s1.substring(i), s2.substring(0, j))) {
                // 서로 스크램블된 문자열이라면 true를 리턴한다.
                map.put(s1 + s2, true);
                return true;
            }
        }
        // 자른 결과중 그무엇도 스크램블된 문자열이 아니라면 false를 리턴한다.
        map.put(s1 + s2, false);
        return false;
    }
}
