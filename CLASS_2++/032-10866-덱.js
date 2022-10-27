const [N, ...order] = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n');

const deque = [];
let result = "";
let len = 0;
let i = 0;
while (i < N) {
    switch(order[i]) {
        case 'pop_front' :
            if (!len) result += '-1\n';
            else {
                result += `${deque.shift()}\n`;
                len--;
            }
            break;
        case 'pop_back' :
            if (!len) result += '-1\n';
            else {
                result += `${deque.pop()}\n`;
                len--;
            }
            break;
        case 'size' :
            result += `${len}\n`
            break;
        case 'empty' :
            if (!len) result += '1\n';
            else result += '0\n';
            break;
        case 'front' :
            if (!len) result += '-1\n';
            else result += `${deque[0]}\n`;
            break;
        case 'back' :
            if (!len) result += '-1\n';
            else result += `${deque[len-1]}\n`;
            break;
        default :
            const [where, value] = order[i].split(' ');
            if (where === 'push_front') deque.unshift(value);
            else deque.push(value);
            len++;
            break;
    }
    i++;
}

console.log(result);