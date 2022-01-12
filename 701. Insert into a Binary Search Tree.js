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
 * @param {number} val
 * @return {TreeNode}
 */
/*
  트리에 아무 노드도 없을때, 노드가 한개가 있을때 예외처리 확실히 해야한다!
*/
var insertIntoBST = function(root, val) {
    
    if (!root) return new TreeNode(val);
    
    if (root.left === null && root.val > val) {
        root.left = new TreeNode(val);
        return root;
    }
        
    if (root.right === null && root.val < val) {
        root.right = new TreeNode(val);
        return root;
    }
    
    if (root.val > val) {
        insertIntoBST(root.left, val);
    } else {
        insertIntoBST(root.right, val);
    }
    
    return root;
};
