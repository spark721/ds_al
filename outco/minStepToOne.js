
// Given an input of a positive integer, 
// find and return the lowest number of operations to reach 1.
// Return 0 if the input is 1.
// Only 3 types of operations allowed.
//     1. subtract by 1
//     2. divide by 3
//     3. divide by 2

// Test cases,
// 10   => 3
// 5    => 3
// 11   => 4
// 37   => 5
// 405  => 7
// 600  => 9
// 5678 => 14
// 9955 => 14
// 1000000  => 19
// 1234567  => 21
// 10000000 => 22



const minStepsToOneMemo = (n) => {
    // *** Tree ***
    // Helper recursion approach
    // Time: O(K^n), exponential

    // Optimizable with memoiization (eleminate duplicate operation)
    // Dynamic Programming
    // Optimized Time: O(n)
    // 1) Create cache
    // 2) Check cache
    // 3) Write to cache
    // Still unable to process large input due to limit of the callstack

    // const cache = {};   // 1) Create cache
    const traverse = (cur) => {
        if (cur in cache) return cache[cur];    // 2) Check cache
        if (cur === 1) return 0;

        // subtract 1
        let option = traverse(cur - 1);

        // divide 3
        if (cur % 3 === 0) {
            let divide3 = traverse(cur / 3);
            option = Math.min(option, divide3);
        };

        // divide 2
        if (cur % 2 === 0) {
            let divide2 = traverse(cur / 2);
            option = Math.min(option, divide2);
        };

        cache[cur] = option + 1;    // 3) Write to cache
        return option + 1;
    };

    return traverse(n);
};

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 



const minStepsToOneTab = (n) => {

    // *** Tabulation ***
    // Time and Space: O(N)
    //  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
    // [n, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3, ...]

    // let result = new Array(n + 1);
    if (result[n] !== undefined) return result[n];
    result[1] = 0;

    for (let i = 2; i < n + 1; i += 1) {
        // subtract 1
        let option = result[i - 1];

        // divide 3
        if (i % 3 === 0) {
            let divide3 = result[i / 3];
            option = Math.min(option, divide3);
        };

        // divide 2
        if (i % 2 === 0) {
            let divide2 = result[i / 2];
            option = Math.min(option, divide2);
        };

        result[i] = option + 1;
    };

    return result[n];
};


// in case of calling this function multiple times,
// best optimize it by placing either cache or tab memory 
// outside of function

const cache = {};    // cache being outside of the function
let result = new Array(600 + 1);  // tab being outside of the function


// test case n: 600
// calling the function 1000 times
console.log(`Case of n=600, calling 1000 times`);
console.time("MEMOIZATION MANY");
for (let i = 0; i < 1000; i++) {
  minStepsToOneMemo(600);
}
console.timeEnd("MEMOIZATION MANY");

console.time("TABULATION MANY");
for (let i = 0; i < 1000; i++) {
  minStepsToOneTab(600);
}
console.timeEnd("TABULATION MANY");


// calling the function 10000 times
console.log(`\nCase of n=600, calling 10000 times`);
console.time("MEMOIZATION MANY");
for (let i = 0; i < 10000; i++) {
  minStepsToOneMemo(600);
}
console.timeEnd("MEMOIZATION MANY");

console.time("TABULATION MANY");
for (let i = 0; i < 10000; i++) {
  minStepsToOneTab(600);
}
console.timeEnd("TABULATION MANY");


// calling the function 100000 times
console.log(`\nCase of n=600, calling 100000 times`);
console.time("MEMOIZATION MANY");
for (let i = 0; i < 100000; i++) {
  minStepsToOneMemo(600);
}
console.timeEnd("MEMOIZATION MANY");

console.time("TABULATION MANY");
for (let i = 0; i < 100000; i++) {
  minStepsToOneTab(600);
}
console.timeEnd("TABULATION MANY");


// calling the function 1000000 times
console.log(`\nCase of n=600, calling 1000000 times`);
console.time("MEMOIZATION MANY");
for (let i = 0; i < 1000000; i++) {
  minStepsToOneMemo(600);
}
console.timeEnd("MEMOIZATION MANY");

console.time("TABULATION MANY");
for (let i = 0; i < 1000000; i++) {
  minStepsToOneTab(600);
}
console.timeEnd("TABULATION MANY");

