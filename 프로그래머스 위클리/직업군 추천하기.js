function solution(table, languages, preference) {
    var answer = '';
    let jobScoreObj = {        
        SI: {},
        CONTENTS:{},
        HARDWARE: {},
        PORTAL: {},
        GAME: {},
    };
    let resultScore = {
        SI: 0,
        CONTENTS: 0,
        HARDWARE: 0,
        PORTAL: 0,
        GAME: 0,
    };
    
    Object.keys(jobScoreObj).forEach((cate, idx) => {
        ["JAVA", "JAVASCRIPT", "C", "C++" ,"C#" , "SQL", "PYTHON", "KOTLIN", "PHP"].forEach(lang => {
            jobScoreObj[cate][lang] = 0;    
        })
    });
    // console.log(jobScoreObj)
    for (let jobScore of table) {
        const jobScoreList = jobScore.split(" ");
        const job = jobScoreList[0];
        const scores = jobScoreList.slice(1);
        
        scores.forEach((sc, idx) => {
           jobScoreObj[job][sc] = (5 - idx) ; 
        });
    }
    
    languages.forEach((lang, idx) => {
        Object.keys(jobScoreObj).forEach((job) => {
            resultScore[job] += jobScoreObj[job][lang] * preference[idx];
        })
        
    })
    
    return Object.entries(resultScore).sort((a, b) => {
        if (a[1] > b[1]) return -1;
        if (a[1] < b[1]) return 1;
        
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
    })[0][0];
}
