const string = require('fs').readFileSync(
    'test.txt'
).toString().trim().split("\n");

let result = "";
string.forEach((ele) => {
    let stack = [];
    for (let i = 0; i < ele.length; i++) {
        const ch = ele[i];
        // console.log(i, ele.charAt(i))
        if (ch === '(' || ch === '[') {
            stack.push(ch);
        }
        else if (ch === ')') {
            if (stack[stack.length-1] === '(') {
                stack.pop();
            } else {
                result += "no\n";
                return;
            }
        }
        else if (ch === ']') {
            if (stack[stack.length-1] === '[') {
                stack.pop();
            } else {
                result += "no\n";
                return;
            }
        }
        else if (ch === '.') {
            if (i !== 0 && i === ele.length-1) {
                if (!stack.length) result += "yes\n";
                else result += "no\n";
                return;
            }
        }
    }
})

console.log(result.trim())