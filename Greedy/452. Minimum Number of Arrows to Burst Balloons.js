/**
 * @param {number[][]} points
 * @return {number}
 */
/*
  풍선 위치의 순회를 돌면서 풍선의 오른쪽 끝지점을 기준으로 풍선을 터뜨려야 가장 많은 풍선을 터뜨릴수 있다.
  끝지점보다 작은 곳에서 화살을 쏘게되면 그것에서 큰 곳에서 시작하는 풍선이 있을때 결국 두번 화살을 쏘게 되기때문에 손해이다.
  풍선의 왼쪽 지점을 기준으로 정렬을 하였지만, 
  오른쪽 지점을 기준으로 정렬을 하면 현재 풍선보다 크기가 작아 품안에 품을수 있는 풍선이 나오는 경우까지 고려하지 않아도 된다.
  
  순회를 돌면서 풍선의 오른쪽을 기준으로 그것보다 시작점이 작은 풍선들은 다 터트릴수 있다.
  시작점이 현재의 최적끝점보다 큰 풍선이 나오면 그 풍선의 끝점으로 현재의 최적 끝점을 업데이트 한다.
*/
var findMinArrowShots = function(points) {
    points.sort((a, b) => a[0] - b[0]);
    
    let curShoot = points[0][1];
    let arrowCnt = 1;
    
    for (point of points) {
        if (point[0] < curShoot && point[1] < curShoot) {
            curShoot = point[1];
        }
        
        if (point[0] > curShoot) {
            curShoot = point[1];
            arrowCnt++;
        }
    }
    
    return arrowCnt;
};
