// https://www.acmicpc.net/source/30573967
// Map() 사용
const fs = require('fs');
const stdin = fs.readFileSync(
    'test.txt'
    ).toString().split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

console.log(Solution());

function Solution() {
    const N = Number(input());
    const temp = input().split(' ').map(Number);

    const cardNum = new Map();

    for (let i = 0; i < N; i++) {
        const num = temp[i];

        if (cardNum.has(num)) {
            cardNum.set(num, cardNum.get(num) + 1);
        } else {
            cardNum.set(num, 1);
        }
    }

    const M = Number(input());
    const findNum = input().split(' ').map(Number);

    const result = [];

    for (let i = 0; i < M; i++) {
        const num = findNum[i];a

        if (cardNum.has(num)) {
            result.push(cardNum.get(num));
        } else {
            result.push(0);
        }
    }

    return result.join(' ');
}
