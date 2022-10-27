const input = require('fs').readFileSync(
	'/dev/stdin'
).toString().trim().split(' ');

let [a, b, c] = input;
let A = BigInt(a);
let B = BigInt(b);
let C = BigInt(c);
// console.log('A', 'B', 'C', A, B, C);
// 2147483647 = 2**31-1

function divideAndConquer(A, B, C) {
    if (B == 1) return A % C;
    
    else {
        let temp = divideAndConquer(A, B / BigInt(2), C);
        if (B % BigInt(2) == 0) return temp * temp % C;    // B가 짝수인 경우
        else return temp * temp * A % C;   // B가 홀수인 경우
    }   
}

console.log(divideAndConquer(A, B, C).toString());