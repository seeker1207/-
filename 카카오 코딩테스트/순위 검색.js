function solution(info, query) {
    let result = [];
    const lans = ['cpp', 'java', 'python'];
    const bfs = ['backend', 'frontend'];
    const ages = ['junior', 'senior'];
    const souls = ['chicken', 'pizza'];
    
    let hash = new Array(3).fill(0).map(
                    () => new Array(2).fill(1).map( 
                        () => new Array(2).fill(2).map( 
                            () => new Array(2).fill(null).map(() => [])
                        )));
    
    
    info.forEach((elm) => {
        const [lan, bf, age, soul, score] = elm.split(' ');
        hash[lans.indexOf(lan)][bfs.indexOf(bf)][ages.indexOf(age)][souls.indexOf(soul)].push(score);
        
    })

    lans.forEach((_, idx) => {
        bfs.forEach((_, idx2) => {
            ages.forEach((_, idx3) => {
                souls.forEach((_, idx4) => {
                    hash[idx][idx2][idx3][idx4] = hash[idx][idx2][idx3][idx4].sort((a, b) => a - b);
                })
            })
        })
    })
    // console.log(hash[2][1][1][0])
    
    const getCntIsHigher = (num, list) => {
        
        if (list.length == 0) return 0;
        
        let [left, right] = [0, list.length];
        
        while (left < right) {          
            let middle = Math.floor((left + right) / 2);
            if (num > parseInt(list[middle])) left = middle + 1;
            else right = middle;
            
        }
        
        return list.length - left;
    }
    
    query.forEach((q) => {
        let [lan, bf, age, slAndScore] = q.split(' and ');
        let [sl, score] = slAndScore.split(' ');
        let cnt = 0;
        
        lan = lan === '-' ? [0, 1, 2] : [lans.indexOf(lan)];
        age = age === '-' ? [0, 1] : [ages.indexOf(age)];
        bf = bf === '-' ? [0, 1] : [bfs.indexOf(bf)];
        sl =  sl === '-' ? [0, 1]: [souls.indexOf(sl)];
        
        // console.log(q, lan, age, bf, sl)
        
        lan.forEach((l) => {
            bf.forEach((b) => {
                age.forEach((a) => {
                    sl.forEach((s) => {
                        cnt += getCntIsHigher(score, hash[l][b][a][s]);
                    })
                
                })
            })
        })
        
        result.push(cnt)
    })
    
    
    return result;
}
