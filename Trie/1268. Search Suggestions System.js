/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */

/*
  트라이 구조로 단어들을 인서트한뒤,
  트라이를 순회하면서 각각의 단어를 추출한다음 리턴하면 된다.
*/
class Trie {
    startNode = {isEnd: false};
    curMatchWord = '';
    bufferOfResult = [];

    insert(word) {
        let curNode = this.startNode;
        for (let char of word) {
            if (!curNode[char]) {
                curNode[char] = {isEnd: false};
            }
            curNode = curNode[char];
        }
        curNode.isEnd = true;
    }

    match(word) {
        let root = this.startNode;
        this.bufferOfResult = [];
        
        for (let char of word) {
            if (!root) {
                return this.bufferOfResult;
            }
            root = root[char];
        }
        
        this.dfs(root, word);
        
        return this.bufferOfResult;
    }


    dfs(curNode, curWord) {
        if (this.bufferOfResult.length === 3) return;
        
        if (!curNode) return;
        
        if (curNode.isEnd) {
            // console.log(curWord);
            this.bufferOfResult.push(curWord);
        }
        
        
        for (let char in curNode) {
                this.dfs(curNode[char], curWord + char);    
        }
        
    }
}
var suggestedProducts = function(products, searchWord) {
    const result = [];
    
    products.sort();
    
    const trie = new Trie();
    for (let product of products) {
        trie.insert(product);
    }
       
    let matchWord = ''
    for (let char of searchWord) {
        matchWord += char;
        result.push(trie.match(matchWord));
    
    }
    return result;
};
