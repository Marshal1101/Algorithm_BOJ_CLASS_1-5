const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const cardCnt = {};
const N = +input[0];
const card = input[1].split(' ').map(Number)
card.forEach((num) => {
    if (cardCnt[num]) {
        cardCnt[num] += 1;
    } else {
        cardCnt[num] = 1;
    }
});
const M = +input[2];
const nums = input[3].split(' ').map(Number);

// console.log('cardCnt', cardCnt)
const cardSet = new Set(card)
// console.log('cardSet', cardSet); 
const newCard = [...cardSet].sort((a, b) => a - b);
// console.log('newCard', newCard);

let result = "";
nums.forEach((num) => {
    let left = 1;
    let right = newCard.length-1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (num === newCard[mid]) {
            result += `${cardCnt[num]} `;
            return;
        }
        if (num > newCard[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    result += '0 ';
    return;
})

console.log(result)