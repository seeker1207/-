function solution(new_id) {
    let newId = '';
    
    const lowerId = new_id.toLowerCase();
    const removedId = lowerId.replace(/[^a-z0-9-_.]/g,'');
    let dotId = removedId;
    while (/[.][.]/g.test(dotId)) {
        dotId = dotId.replace(/[.][.]/g,'.');    
    }
    while (dotId[0] === '.') dotId = dotId.slice(1);
    while ((dotId[dotId.length-1] === '.')) dotId = dotId.slice(0, dotId.length - 1);
    if (dotId === '') dotId = 'a';
    newId = dotId;
    if (newId.length >= 16) newId = newId.slice(0, 15);
    if (newId[newId.length-1] === '.') newId = newId.slice(0, newId.length - 1);
    if (newId.length <= 2) while(newId.length !== 3) newId += newId[newId.length - 1];
    
    return newId;
}
