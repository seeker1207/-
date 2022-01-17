/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
/*
  패턴과 문자열 리스트를 1대1관계로 매핑시켜야한다.
  따라서 두개의 hash 구조로 저장을 하여 해결함.
*/
var wordPattern = function(pattern, s) {
    let ptToWord = {};
    let wordToPt = {};
    
    let sList = s.split(' ');
    
    if (sList.length !== pattern.length) return false;
    
    for (let i = 0; i < pattern.length; i++) {
        const [curPt, curWord] = [pattern[i], sList[i]];
        
        if (curPt in ptToWord && ptToWord[curPt] !== curWord) {
            return false;
        }
        
        if (curWord in wordToPt && wordToPt[curWord] !== curPt) {
            return false;
        }
        
        ptToWord[curPt] = ptToWord[curPt] || curWord;
        wordToPt[curWord] = wordToPt[curWord] || curPt;
    }
    
    return true;
};
