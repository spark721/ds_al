
// LeetCode
// # 253
// Medium


/*

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

*/


const minMeetingRooms = function(a) {
    let start = a.slice().sort((a, b) => {
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
    });
    
    let end = a.slice().sort((a, b) => {
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
    });
    
    let count = 0;
    
    let n = 0;
    let i = 0;
    
    while (i < start.length) {
        if (start[i][0] < end[n][1]) {
            count += 1;
        } else if (start[i][0] >= end[n][1]) {
            n += 1;
        }
        
        i += 1;
    };
    
    return count;
};