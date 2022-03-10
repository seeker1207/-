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
    끝 노드에 도달했을 시 가장 깊은 레벨과 비교하여 sum에 해당 노드값을 더할지 초기화할지를 결정한다.
*/
var deepestLeavesSum = function(root, level = 1) {
    let sum = 0;
    let deepestLv = 0;
    
    let getSum = (root, level = 1) => {
        if (!root) return;
    
        if (!root.left && !root.right){
            if (level > deepestLv) sum = root.val;
            if (level === deepestLv) sum += root.val;

            deepestLv = Math.max(level, deepestLv);
            // console.log(level, deepestLv, root.val, sum)
        }   

        getSum(root.left, level + 1);
        getSum(root.right, level + 1);

        return sum;
    }

    return getSum(root);
};
