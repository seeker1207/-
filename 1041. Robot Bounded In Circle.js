/**
 * @param {string} instructions
 * @return {boolean}
 */
var isRobotBounded = function(instructions) {
    const move = {
        'N': [0, 1], 
        'E': [1, 0],
        'W': [-1, 0],
        'S': [0, -1],
    }
    
    const getDir = (dir, lOrR) => {
        if (lOrR === 'G') return dir;
        switch (dir) {
            case 'N': 
                if(lOrR === 'L') return 'W';
                else return 'E';
            case 'E':
                if(lOrR === 'L') return 'N';
                else return 'S';
            case 'W':
                if(lOrR === 'L') return 'S';
                else return 'N';
            case 'S':
                if(lOrR === 'L') return 'E';
                else return 'W';
        }
        
    };
    
    let curDir = 'N';
    let curPos = [0, 0];
    
    if (instructions[0] !== 'G') {
        curDir = getDir('N', instructions[0]); 
    } else {
        curPos = [0, 1];
    }
    
    let insIdx = 1;
    
    while (insIdx < instructions.length) {
        const curIstr = instructions[insIdx];
        
        if (curIstr === 'G') {
            curPos = [curPos[0] + move[curDir][0], curPos[1] + move[curDir][1]];
        } else {
            curDir = getDir(curDir, curIstr);
        }
        
        // if (curPos[0] === 0 && curPos[1] === 0) return true;
        
        insIdx++;
    }
    
    console.log(curPos)
    if (curDir !== 'N' || (curPos[0] === 0 && curPos[1] === 0)) return true;
    
    return false;
};
