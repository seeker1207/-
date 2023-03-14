/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int sum = 0;

    public int sumNumbers(TreeNode root) {
        dfs(root, "");
        return this.sum;
    }

    public void dfs(TreeNode root, String currNum) {
        if (root.left == null && root.right == null) {
            this.sum += Integer.valueOf(String.valueOf(currNum) + root.val);
            return;
        }

        if (root.left != null) {
            dfs(root.left, currNum + String.valueOf(root.val));
        }
        if (root.right != null) {
            dfs(root.right, currNum + String.valueOf(root.val));    
        }
        
    }
}
