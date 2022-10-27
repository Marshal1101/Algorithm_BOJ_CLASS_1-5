let [N, M, ch] = require('fs').readFileSync(
    'z1.in'
).toString().trim().split("\n");

N = +N
if (M > 0) ch = ch.split(' ').map(Number)
function check(num) {
    arr = [...String(num)];
    for (const i of arr) {
        if (ch.includes(+i)) return false
    }
    return true
}

let result = Math.abs(N - 100)
for (let i = 0; i < 1000001; i++) {
    if (M == 0 || check(i)) {
        temp = String(i).length + Math.abs(i - N) 
        if (temp < result) result = temp
    }
}
console.log(result)