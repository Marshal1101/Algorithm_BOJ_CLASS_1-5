const serial = require('fs').readFileSync('test.txt').toString().trim().split(' ').map(Number);

function verification(serial) {
    const sum = serial.reduce((prev, curr) => 
        prev + curr * curr
    , 0);
    return sum % 10;
}

console.log(verification(serial));