let [nk, ...arr] = require('fs').readFileSync(
    'z1.in'
).toString().trim().split('\n')

let [N, K] = nk.split(' ').map(Number);

let dp = Array.from({length: (N+1)}, () => new Array(K+1).fill(0));
// console.log(dp)

for (let i = 1; i < N+1; i++) {

    const [W, V] = arr[i-1].split(' ').map(Number);

    for (let j = 1; j < K+1; j++) {
        let a = dp[i-1][j]
        let b = dp[i-1][j-W] + V
        if (j >= W) {
            dp[i][j] = a > b ? a : b
        } else {
            dp[i][j] = a
        }
    }
}

// console.log(N, K)
console.log(dp[N][K])