let [N, ...order] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const queue = [];
let result = "";
let len = 0;
let i = 0;
while (i < N) {
    switch(order[i]) {
        case 'pop' :
            if (len === 0) {
                result += '-1\n';
            } else {
                result += `${queue.shift()}\n`;
                len--;
            }
            break;
        case 'size' :
            result += `${len}\n`;
            break;
        case 'empty' :
            if (!len) {
                result += '1\n';
            } else {
                result += '0\n';
            }
            break;
        case 'front' :
            if (!len) {
                result += '-1\n';
            } else {
                result += `${queue[0]}\n`;
            }
            break;
        case 'back' :
            if (!len) {
                result += '-1\n';
            } else {
                result += `${queue[len-1]}\n`;
            }
            break;
        default :
            queue.push(order[i].split(' ')[1])
            len++;
            break;
    }
    i++;
}

console.log(result);