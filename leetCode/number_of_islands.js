
// LeetCode
// # 200
// Medium

/*

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

*/

/*

iterate through every element.
If ele is '1', increment count and call dfs.

If cur is '1', mutate the original
call dfs on all four direction of the cur

*/



var numIslands = function(grid) {
    let islands = 0;

    function dfs(row, col) {
    	if (
    		row < 0 ||
    		row >= grid.length ||
    		col < 0 ||
    		col >= grid[0].length
    		) return;

    	if (grid[row][col] === '1') {
    		grid[row][col] = '#';
    		dfs(row + 1, col);
    		dfs(row - 1, col);
    		dfs(row, col + 1);
    		dfs(row, col - 1);
    	};
    };

    for (let i = 0; i < grid.length; i += 1) {
    	let row = grid[i];

    	for (let n = 0; n < row.length; n += 1) {
    		let cur = grid[i][n];

    		if (cur === '1') {
    			islands += 1;
    			dfs(i, n);
    		};
    	};
    };


    return islands;
};


