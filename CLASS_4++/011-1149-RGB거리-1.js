// DFS 시간초과

let [N, ...arr] = require('fs').readFileSync(
    'dev/stdin'
).toString().trim().split('\n')

N = +N
const RGBCost = arr.map((house) => house.split(' ').map(Number))
let minimalCost = 1000*N

function dfs(houseNum, cost, formerColor) {

    if (cost > minimalCost) return;

    if (houseNum === N) {
        if (cost < minimalCost) {
            minimalCost = cost;
        }
        return;
    }

    for (let color = 0; color < 3; color++) {
        if (color !== formerColor) {
            dfs(houseNum + 1, cost + RGBCost[houseNum][color], color)
        }
    }
}

dfs(0, 0, -1)
console.log(minimalCost)