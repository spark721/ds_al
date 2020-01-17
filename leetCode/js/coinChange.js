function coinChange(coins, amount) {
    // tabulation, dynamic programming
    // initialize an array of size = amount + 1
    // build up the array starting from 1
    // for each amount, check against all the coins
    // if a coin is less than an amount
    // subtract a coin value from amount then
    // look at the arr[amount-coin], compare & update
    // return arr[amount]

    if (amount === 0) return 0; // edge case

    const arr = new Array(amount + 1).fill(amount + 1);
    arr[0] = 0;

    for (let i = 1; i < arr.length; i += 1) {
        for (let j = 0; j < coins.length; j += 1) {
            let coin = coins[j];

            if (i === coin) {
                arr[i] = 1;
                break;
            } else if (i > coin) {
                let prev = arr[i - coin];
                arr[i] = Math.min(prev + 1, arr[i]);
            };
        };
    };

    return arr[amount] === amount + 1 ? -1 : arr[amount];
};



console.log(coinChange([1,2,5], 11));   // => 3
console.log(coinChange([2], 3));   // => -1
console.log(coinChange([186, 419, 83, 408], 6249));   // => 20
