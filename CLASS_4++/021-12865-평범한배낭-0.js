// https://www.acmicpc.net/source/38124807

let fs = require('fs');
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [N,K] = input.shift().split(' ').map(v =>+v);
//N: 물품수, K:최대무게
let map = input.map(ele => ele.split(' ').map(v =>+v)).filter(v => K-v[0]>=0)
//[w,v]

let dp = new Array(K+1).fill(0);
let answer =0;
map.sort(function(a,b){
    return a[0]-b[0]
})//무게에 따라 정리

map.forEach(el =>{
    const [w,v] = el;
    //최대무게는 K
    //K-w= 남은 최대무게;
    for(let i=K-w; i>=0;i--){
        if(i==0){
            dp[w] = Math.max(dp[w],v);
            answer = Math.max(dp[w],answer)
        }else{
            if(dp[i]>0){
                dp[i+w] = Math.max(dp[i+w],dp[i]+v)
                answer = Math.max(dp[i+w],answer)
            }
        }
    }
})
console.log(answer)
