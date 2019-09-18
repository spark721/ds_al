
// LeetCode > Cisco
// # 102
// Medium


/*

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

*/

var levelOrder = function(root) {
    let result = [];
    if (!root) return result;
    let que = [ [ root ] ];
    
    while (que.length) {
        let curLevel = que.shift();
        let newLevel = [];
        let nextLevel = [];
        
        curLevel.forEach( node => {
            if (node) {
                newLevel.push( node.val );
                if (node.left) nextLevel.push( node.left );
                if (node.right) nextLevel.push( node.right );
            };
        });
        
        if (nextLevel.length) que.push( nextLevel );
        result.push( newLevel );
    };
    
    return result;
};