/**
 * @param {string} path
 * @return {string}
 */
/*
  스택을 떠올렸다면 꽤 빨리 풀수 있는 문제.
  상위일때 pop 해서 유효한 디렉토리 이름들만 남긴다.
*/
var simplifyPath = function(path) {
    let realPath = path.replace(/[/]+/g,'/').split('/');
    let st = [];
    
    for (let dir of realPath) {
        if (dir === '') continue;
        if (dir === '..') {
            st.pop();
        } else if (dir === '.') {
            continue;
        } else {
            st.push(dir);
        }
        
    }
    
    return '/' + st.join('/');
};
