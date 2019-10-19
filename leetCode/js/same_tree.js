
// LeetCode
// 100
// Easy

// Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

//     Example 1:

// Input: 1         1
//     / \       / \
// 2   3     2   3

// [1, 2, 3], [1, 2, 3]

// Output: true

// Example 2:

// Input: 1         1
//     /           \
// 2             2

// [1, 2], [1, null, 2]

// Output: false

// Example 3:

// Input: 1         1
//     / \       / \
// 2   1     1   2

// [1, 2, 1], [1, 1, 2]

// Output: false


// BFS approach
// construct an array per tree
// compare the indices
// Time: O(n)
// Space: O(n)

function isSameTree(p, q) {
    if (!p && !q) return true;
    if (!p || !q) return false;
    if (p.val !== q.val) return false;
    
    function bfs(node) {
        let que = [node];
        let result = [];

        while (que.length) {
            let n = que.shift();
            result.push(n ? n.val : null);

            if (n) {
                que.push(n.left ? n.left : null);
                que.push(n.right ? n.right : null);
            }
        }

        return result;
    }

    let pArr = bfs(p);
    let qArr = bfs(q);

    for (let i = 0; i < pArr.length; i += 1) {
        if (pArr[i] !== qArr[i]) return false;
    }

    return true;
}


