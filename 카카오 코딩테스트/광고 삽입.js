function solution(play_time, adv_time, logs) {
    var answer = '';
    const allSec = getSec(play_time);
    const advSec = getSec(adv_time);
    let timeArray = new Array(allSec + 1).fill(null).map(() => 0);
    
    for (let log of logs) {
        const [st, end] = log.split('-');
        timeArray[getSec(st)] += 1;
        timeArray[getSec(end)] -= 1;
    }

    for (let i=1; i < timeArray.length; i++) {
        timeArray[i] += timeArray[i-1];
    }

    for (let j=1; j < timeArray.length; j++) {
        timeArray[j] += timeArray[j-1];
    }

    let maxTime = timeArray[advSec - 1];
    let rt = 0;
    for (let k = advSec - 1; k < timeArray.length; k++) {
        if (timeArray[k] - timeArray[k - advSec] > maxTime) {
            maxTime = timeArray[k] - timeArray[k - advSec];
            rt = k - advSec + 1
        }
    }

    return getTimeStr(rt);
}

function getSec(playTime) {
    let [hour, min, sec] = playTime.split(':');
    return +hour * 3600 + +min * 60 + +sec;
}

function getTimeStr(sec) {
    let hour = sec / 3600 >> 0;
    let minute = sec % 3600 / 60 >> 0;
    let _sec = sec % 3600 % 60;

    hour = hour > 9 ? hour : '0' + hour;
    minute = minute > 9 ? minute : '0' + minute;
    _sec = _sec > 9 ? _sec : '0' + _sec;

    return hour + ':' + minute + ':' + _sec;
}
