/**
 * @param {string[]} words
 * @param {string[]} puzzles
 * @return {number[]}
 */

/*
    words와 puzzle을 일일히 비교하면 시간초과가 난다.
    따라서 words를 비트마스킹해서 그 비트값을 십진수로 변환한 값을 키값으로 활용한 맵 구조를 이용한다.
    (비트마스크 십진수 값을 이용하면 다른 word라도 중복되는 값이 분명히 존재할수 있다.)
    그렇게 하여 퍼즐을 탐색할때 모든 words를 돌 필요가 없도록 한다.
    
    퍼즐을 돌면서 해당 퍼즐을 비트마스크 십진수 값으로 변환한다.
    이 퍼즐의 비트마스크의 서브마스크들을 찾는다. (word의 단어들이 퍼즐에 모두 있어야하므로)
    1. 이 서브마스크들 중 앞서 구한 맵 구조에 같은값을 가진 키가 있고,
    2. 해당 퍼즐의 첫번째 글자를 가지고 있는 서브마스크가 있다면,
    그 값을 카운트해준다. (조건에 만족하는 word들 카운트.)
    
    비트마스크의 서브마스크를 찾을떄 submask - 1 & puzmask 알고리즘을 이용한다.
    서브마스크는 결국 비트마스크의 값보다 작다. 그렇기 때문에 -1을 해주면 모든 경우의 수를 탐색할수 있다.
    또한, 이진수에서 -1을 해주게되면 가장 오른쪽의 1이 지워지고  그 이후엔 모든 오른쪽 비트가 1이 되며 오른쪽으로 당겨진다. 
    그다음 기존의 mask를 씌워주게되면 결국 그 상황에서 구할수 있는 가장 높은 숫자의 서브마스크가 나오게된다.
*/
var findNumOfValidWords = function(words, puzzles) {
    let ret = [];
    let bitMap = new Map();
    
    let getBitmask = (str) => {
        let ret = 0;
        for (let s of str) {
            ret |= 1 << s.charCodeAt(0) - 'a'.charCodeAt(0);
        }
        return ret;
    }
    
    words.forEach((word) => {
        let wordMask = getBitmask(word);
        if (bitMap.has(wordMask)) {
            bitMap.set(wordMask, bitMap.get(wordMask) + 1);
        } else {
            bitMap.set(wordMask, 1);
        }
    })
    
    
    for (let puz of puzzles) {
        let puzMask = getBitmask(puz);
        let firstIdx = puz[0].charCodeAt(0) - 'a'.charCodeAt(0);
        let cnt = 0;
        
        for (let submask = puzMask; submask > 0; submask = (submask - 1) & puzMask) {
            if (bitMap.has(submask) && (submask & (1 << firstIdx))) {
                cnt += bitMap.get(submask);
            }
        }
        
        ret.push(cnt);
    }
    
    return ret;
    
};
