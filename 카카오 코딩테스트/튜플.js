function solution(s) {
    let sArray = s.slice(2, s.length - 2).split('},{');
    let sHash = new Array(501).fill(0);
    let sSet = new Set();
    let result = [];
    
    sArray = sArray.map(
        (elm) => elm.split(',')).sort((a, b) => a.length - b.length);
    
    sArray.forEach((elm, idx) => {
        elm.forEach((num) => {
            if (!sSet.has(num)) {
            sSet.add(num);
            result.push(+num)
        }    
        })
    })

    
    return result;
}
