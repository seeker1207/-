
function matching(matchList) {

    // tp: 지금 검사하고 있는 target index
    // wp: 지금 검사하고 있는 단어의 index
    const isMatch = (word, target, tp, wp) => {

        while (wp < word.length && tp < target.length && (word[wp] === target[tp] || target[tp] !== '*')) {
            tp++;
            wp++;
        }

        // tp가 target 끝에 왔고 wp도 word의 끝에 왔다면 매칭이 다 되었다는 의미 이므로 true;
        if (tp === target.length) {
            return wp === word.length;
        }

        // '*'인 경우 어디까지 단어가 매칭되는 지를 재귀를 통해 찾는다. 매칭되는 경우가 하나라도 있는 경우 true 리턴
        if (target[tp] === '*') {
            for (let i=0; i <= word.length - wp; i++) {
                if (isMatch(word, target, tp+1, wp+i)) {
                    return true;
                }
            }
        }

        return false;

    }
    for (let match of matchList) {
        const [word, target] = match.split(' ');
        console.log(isMatch(word, target, 0, 0))

    }

}
matching(['1 *?*', 'codinging *?ng*ing', 'interview in*', 'apple app?e', 'vanilla vani?a', 'banana ba*na', 'fruits fru*its', 'Love Love*', 'Landvibe L*d?i*e'])




