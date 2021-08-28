function solution(orders, course) {
    var answer = [];
    let courseCnt = {};
    let countMax = {};
    let courseSet = new Set(course);


    const getCombi = (order, nowCombi, start) => {

        const N = nowCombi.length;
        if (courseSet.has(N)) {
            const key = nowCombi;

            if (key in courseCnt) courseCnt[key] += 1;
            else courseCnt[key] = 1;

            if (N in countMax) countMax[N] = Math.max(courseCnt[key], countMax[N]);
            else countMax[N] = courseCnt[key];

        }

        for (let i = start; i<order.length; i++) {
            getCombi(order, nowCombi + order[i], i+1);
        }
    };


    orders.forEach((order) => {
        getCombi(order.split('').sort().join(''), [], 0);   

    })

    return Object.entries(courseCnt)
                .filter((elm) => elm[1] !== 1 && countMax[elm[0].length] === elm[1])
                .map((elm) => elm[0])
                .sort();
}
