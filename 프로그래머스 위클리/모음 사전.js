function solution(word) {
    var answer = 0;
    const UpperAlpha = ['A', 'E', 'I', 'O', 'U'].sort();
    
    let words = {};
    let seq = 1;
    
    let getWords = (word) => {
        if (word !== '')
            words[word] = seq++;
        
        if (word.length === 5) {
            return;
        }
        
        UpperAlpha.forEach((al) => {
            getWords(word + al);
        })
    }
    
    getWords('');
    
    return words[word];
}
