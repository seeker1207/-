/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

/*
    1. memo를 이용한 재귀 방식 풀이
    
    이진 트리 구조에서 한 노드에서 훔칠수 있는 최대값은 
    
    해당 노드에서 훔친다고 가정하면,
    노드의 현재값 + 한단계 건너뛴 노드들의 훔친 최대값들 이다.
    
    해당 노드에서 훔치지 않는다면,
    해당 노드의 자식 노드들의 훔친 최대값을 합한 값이된다.
    
    결과적으로 현재 노드에서 훔칠수 있는 최대값은 
    위 두가지 경우 중 큰값이라고 할 수 있다.
    
    그런데 중복되는 노드들이 발생하므로 해쉬구조를 써서 미리 memo를 해놓아 중복 호출을 방지한다.
    
    2.  dp 배열을 이용한 풀이
    
    그 이전 노드들의 값을 재귀적으로 모두 호출 하지 않고 각 노드마다 
    훔친 경우, 훔치지 않은 경우에 해당하는 최대값을 기록해 놓는다.
    
    현재 노드에서의 최대값은,
    
    해당 노드에서 훔쳤다고 가정하면, 
    그 이전 자식 노드들 중 훔치지 않았을 경우의 값들을 더하고 현재 노드의 값을 더한다.
    
    해당 노드에서 훔치지 않았다면,
    자식 노드들의 훔친 경우와 안훔친 경우 중 큰값 들을 더하면 된다. 
    (현재 노드에서 훔치지 않는다면 그 이전노드에서 훔칠수도 있고 안훔칠 수도 있다.)

*/
const map = new Map();

var rob = function(root) {

    /* 재귀방식 memo 풀이
    if (!root) return 0;
    
    if (map.has(root)) return map.get(root);
    
    let [left, right] = [0, 0];
    
    if (root.left) {
        left = rob(root.left.left) + rob(root.left.right);    
    }
    
    if (root.right) {
        right = rob(root.right.left) + rob(root.right.right);
    }
    
    let maxVal = Math.max(left + right + root.val, rob(root.left) + rob(root.right));
    
    map.set(root, maxVal);
    
    return maxVal;
    */
    
    // dp 풀이
    let getMax = (root) => {
        if (!root) return [0, 0];
        
        let [L, R] = [getMax(root.left), getMax(root.right)];
        
        
        return [Math.max(...L) + Math.max(...R), root.val + L[0] + R[0]];
        
    }
    
    return Math.max(...getMax(root));
    
};
