
function run(arr) {
    let max = -Infinity;
    let sum = arr.reduce((acc, num) => acc + num);
    const queue = [
        { arr: arr.slice(0), dir: 1, sum, i: 1, score: 0 },
        { arr: arr.slice(0), dir: -1, sum, i: 1, score: 0 },
    ];

    while (queue.length) {
        const { arr, dir, sum, score, i } = queue.pop();
        const currScore = i % 2 === 0 ? score - sum : score + sum;

        if (arr.length === 1)
            max = Math.max(max, currScore);

        const removedItem = dir === 1 ? arr.pop() : arr.shift();
        if (arr.length) {
            if (i % 2 === 0) {
                queue.push(
                    {
                        arr: arr.slice(0),
                        dir: 1,
                        sum: sum - removedItem,
                        i: i + 1,
                        score: currScore,
                    },
                    {
                        arr: arr.slice(0),
                        dir: -1,
                        sum: sum - removedItem,
                        i: i + 1,
                        score: currScore,
                    },
                );
            } else {
                queue.push(
                    {
                        arr: arr.slice(0),
                        dir: 1,
                        sum: sum - removedItem,
                        i: i + 1,
                        score: currScore,
                    },
                    {
                        arr: arr.slice(0),
                        dir: -1,
                        sum: sum - removedItem,
                        i: i + 1,
                        score: currScore,
                    },
                )
            }
        }
    }
    return max;
}

testArr1 = [1, 2, 3, 4, 2, 6] // => 13

testArr2 = [7, 0, 38, 17, 1, 3, 49, 48, 48, 48, 6, 43, 27, 2, 12, 35, 6, 3, 37, 15] // => 370

testArr3 = [952359693,
    722064488,
    245254090,
    79065812,
    106495569,
    796253068,
    919116269,
    252407112,
    230251590,
    496353710,
    591692102,
    512543377,
    7831487,
    851022419,
    776752016,
    458896476,
    229332315,
    305941991,
    39719925,
    937535564] // => 7518235472
