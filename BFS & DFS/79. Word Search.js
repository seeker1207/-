/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let [N, M] = [board.length, board[0].length];
    let move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    let wordSearch = (x, y, cnt, visited) => {
        if (word[cnt] !== board[x][y]) return false;
        if (cnt === word.length - 1) return true;
        let ret = false;
        
        for (let mv of move) {
            let [moveX, moveY] = [x + mv[0], y + mv[1]];
            
            if ((moveX < N && moveX >= 0) && (moveY < M && moveY >= 0) ) {
                if (!visited[moveX][moveY]) {
                    visited[moveX][moveY] = 1;
                    ret = ret || wordSearch(moveX, moveY, cnt + 1, visited);
                    visited[moveX][moveY] = 0;
                }
                
            }
        }
        
        return ret;
    }
    
    for (let i=0; i<N; i++) {
        for (let j=0; j<M; j++) {
            let visited = new Array(N).fill(null).map(() => new Array(M).fill(0));
            visited[i][j] = 1
            if (wordSearch(i, j, 0, visited)) return true;
        }
    }
        
    return false
};
