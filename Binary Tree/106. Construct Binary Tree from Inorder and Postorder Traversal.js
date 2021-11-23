/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
/*
    1) postorder의 경우 끝 인덱스가 root 인덱스 이게 된다.
    2) 그렇게 찾은 root 노드 값으로 inorder배열에서 왼쪽 트리노드, 오른쪽 트리노드들을 찾을 수 있다.
    3) 그것을 이용해 postorder에서 왼쪽 트리노드와 오른쪽 트리노드의 범위를 알수 있다.
    4) left [9] , right [15, 7, 20, 3] 여기서 재귀적으로 오른쪽 트리노드들의 루트노드는 또 3인것을 알수 있다.
    5) 이과정을 반복하여 divide & Conquer, 재귀적 방식으로 트리를 완성해나간다. 
    
    이때 postorder에서 찾은 root 노드의 inorder 인덱스를 해쉬맵 구조를 통해 더 빠르게 찾을 수 있다.
    
*/
var buildTree = function(inorder, postorder) {
//     let inOrderMap = new Map();
    
//     inorder.forEach((val, idx) => {
//         inOrderMap.set(val, idx);
//     });
    
    let hash = {};
    for (let i=0;i<inorder.length;i++) hash[inorder[i]] = i;
    
    let idx = postorder.length - 1;
    
    let recur = function(start, end) {
        if (start > end) return null;
        let val = postorder.pop();
        let root = new TreeNode(val);
        root.right = recur(hash[val] + 1, end);
        root.left = recur(start, hash[val] - 1);
        return root;
    }
    
    return recur(0, inorder.length - 1);
    

};
