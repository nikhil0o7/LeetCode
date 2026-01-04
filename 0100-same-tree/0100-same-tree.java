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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return dfs(p,q);
    }

    private boolean dfs(TreeNode one, TreeNode two){
        if(one == null && two == null){
            return true;
        }
        if(one == null || two == null){
            return false;
        }

        if(one.val != two.val){
            return false;
        }

        boolean left = dfs(one.left, two.left);
        boolean right = dfs(one.right, two.right);
        return left && right;
    }
}