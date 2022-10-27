const [A, B] = require('fs').readFileSync('dev/stdin').toString().trim().split(' ').map(Number);
console.log(A + B);