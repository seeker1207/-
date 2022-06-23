/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function(courses) {
    courses.sort((a, b) => a[1] - b[1]);
    
    const maxEndTime = courses[courses.length - 1][1];
    
    const memo = Array(courses.length).fill(null).map(() => Array(maxEndTime + 1).fill(null));
    
    // console.log(memo)
    const getMaxCourse  = (i, time) => {        
        if (i === courses.length) {
            return 0;
        }

        if (memo[i][time] !== null) {
            return memo[i][time];
        }
        
        let taken = 0;
        if (time + courses[i][0] <= courses[i][1]) {
            taken = 1 + getMaxCourse(i + 1, time + courses[i][0]);
        }
        const not_taken = getMaxCourse(i + 1, time)
        memo[i][time] = Math.max(taken, not_taken);
        
        return memo[i][time];
    }
    
    return getMaxCourse(0, 0)
};
