let [N, ...arr] = require('fs').readFileSync(
    'z1.in'
).toString().trim().split('\n')

N = +N
step = Array(N)
arr.forEach((line, i) => {
    step[i] = line.split(' ').map(Number);
})

for (let i = 1; i < N; i++) {
    for (let j = 0; j < i+1; j++) {
        if (j === 0) step[i][j] = step[i-1][j] + step[i][j]
        else if (j === i) step[i][j] = step[i-1][j-1] + step[i][j]
        else step[i][j] = Math.max(step[i-1][j-1], step[i-1][j]) + step[i][j]
    }
}

console.log(Math.max(...step[N-1]))