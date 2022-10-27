let [N, arr] = require('fs').readFileSync("test.txt").toString().trim().split('\n');
N = +N;
const numbers = arr.split(' ').map(Number);
let minNum = numbers[0];
let maxNum = numbers[0];
numbers.forEach((num) => {
    if (num > maxNum) maxNum = num;
    else if (num < minNum) minNum = num;
})

console.log(minNum, maxNum);