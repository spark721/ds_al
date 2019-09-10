
// LeetCode
// # 199
// Medium


/*

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

*/



const rightSideView = function(root) {
    let result = [];
    if (!root) return result;

    const dfs = (node, level) => {
    	if (level === result.length) result.push(node.val);

    	if (node.right) dfs(node.right, level + 1);
    	if (node.left) dfs(node.left, level + 1);
    };

    dfs(root, 0);

    return result;
};

