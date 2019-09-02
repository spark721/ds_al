
// LeetCode > Cisco
// # 247
// Medium


/*
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
*/


/**
 * @param {number} n
 * @return {string[]}
 */
var findStrobogrammatic = function(n) {
    let arr = ["11", "69", "88", "96"];
    if (n === 1) return ["0", "1", "8"];
    if (n === 2) return arr;
    
    let result = [];
    let prev = null;
    
    if (n % 2 === 0) {
        arr.unshift("00");
        prev = findStrobogrammatic(n - 2);
    } else {
        arr = ["0", "1", "8"];
        prev = findStrobogrammatic(n - 1);
    }
    
    prev.forEach( cur => {
        let left = cur.slice(0, Math.trunc(cur.length / 2));
        let right = cur.slice(Math.trunc(cur.length / 2));

        arr.forEach( mid => {
            result.push( left + mid + right );
        });
    });
    
    return result;
};