const solution = (k, userScores) => {
let rankBoard = new Array(k).fill('');
let userScore = userScores.reduce((scoreObj, userSc, idx)=> {
const [id, score] = [userSc.split(' ')[0], userSc.split(' ')[1]];

if (!(id in scoreObj)) scoreObj[id] = [score, idx];
if (id in scoreObj && scoreObj[id] < score) {
scoreObj[id] = [score, idx];
}

return scoreObj;
}, {});

const result = Object.entries(userScore).sort((a, b) => b[1][0] - a[1][0] || a[1][1] - b[1][1])
console.log(Object.entries(userScore))
console.log(result);
console.log(userScore)
console.log(rankBoard);
}


solution(4, ["alex111 100", "cheries2 200", "luna 100", "alex111 120", "coco 300", "cheries2 100"]);
