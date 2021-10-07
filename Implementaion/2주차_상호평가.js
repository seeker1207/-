function solution(scores) {
    var answer = '';
    var score = new Array(scores.length).fill(0);
    var flag = new Array(scores.length).fill(false);
    let getResult = (score) => {
        if (score >= 90) return 'A';
        else if(score >= 80 && score < 90) return 'B';
        else if(score >= 70 && score < 80) return 'C';
        else if(score >= 50 && score < 70) return 'D';
        else return 'F';
    }
    
    let isUnique = (score, list) => {
        let check = false;
        for (let elm of list) {
            if (elm === score) {
                if (!check) check = true;
                else return false;
            }

        }
        return true;
    }
    
    scores = scores[0].map((_, idx) => scores.map((sl) => sl[idx]))

    scores.forEach((scoreList, idx) => {
        let N = scoreList.length;
        let sum = scoreList.reduce((pre, cur) => pre + cur);
        
        if ((scoreList[idx] === Math.max(...scoreList) || scoreList[idx] === Math.min(...scoreList)) && isUnique(scoreList[idx], scoreList)) {
            sum -= scoreList[idx];
            N -= 1;
        }
        answer += getResult(sum / N);
    })

    return answer;
}
