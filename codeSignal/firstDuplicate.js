
// CodeSignal > Interview Practice > Arrays
// Easy

/*
Asked by Google

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than 
the second occurrence of the other number does. 
If there are no such elements, return -1.

Example

    For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

    There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

    For a = [2, 2], the output should be firstDuplicate(a) = 2;

    For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

*/

function firstDuplicate(a) {
    let obj = scanArray(a);
    let arr = Object.values(obj);
    
    let lowest = a.length + 1;
    
    arr.forEach( (cur, i) => {
        if (cur !== "1st" && cur < lowest) {
            lowest = cur;
        }
    });
    
    return a[lowest] ? a[lowest] : -1;
}

function scanArray(a) {
    let obj = {};
    
    for (let i = 0; i < a.length; i += 1) {
        let cur = a[i];
        
        if (obj[cur] === undefined) {
            obj[cur] = "1st";
        } else if (obj[cur] === "1st") {
            obj[cur] = i;
        }
    }
    
    return obj;
}
