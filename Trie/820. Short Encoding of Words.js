/**
 * @param {string[]} words
 * @return {number}
 */
/*
  trie구조로 해당 단어들을 넣는다.
  이때 단어의 끝에 해당하는 노드들을 맵에 미리 저장해둔다.
  단어들을 trie구조로 넣고나서, 맵에 저장해둔 노드들 중 자식이 없는 노드를 찾는다. (자식이 없는 노드들이 suffix가 겹치는 것 중 가장 큰 단어의 노드.)
  해당 노드들의 단어 길이와 '#'을 합한 길이를 더해 결과를 도출한다.
*/

class Trie {
    rootNode = {}
    wordEndNodeMap = new Map();

    insert(word) {
        let curNode = this.rootNode;
        let reversed = Array.from(word).reverse();

        for (let i=0; i<reversed.length; i++) {
            const char = reversed[i];

            if (!curNode[char]) {
                curNode[char] = {};
            } 

            curNode = curNode[char];
        }

        this.wordEndNodeMap.set(curNode, word);
    }

}


var minimumLengthEncoding = function(words) {

    let result = 0;
    const trie = new Trie();

    for (let word of words) {
        trie.insert(word);
    }

    for (let [node, word] of trie.wordEndNodeMap.entries()) {
        if (Object.keys(node).length === 0) {
            result += word.length + 1;
        }
    }

    return result;

};
