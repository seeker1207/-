/*
  크루스칼 알고리즘을 활용한다. 전체 간선의 비용중 가장 작은 것부터 탐색하여 최소신장트리(MST)를 찾는다.
  가장 작은 간선 비용의 끝 노드들이 사이클이 없도록 선택해야하므로, union-find를 사용하여 현재 선택된 간선의 양끝단의 노드가 같은 집합인지 아닌지를 확인한다.
  같은 집합이면 사이클이므로 선택하지 않는다.
  다른 집합이면 두 집합을 합친다. (부모노드 끼리 연결)
*/

function solution(n, costs) {
    var answer = 0;
    let visited = new Set();
    let parent = new Array(n).fill().map((_, idx) => idx);
    
    let getParent = (x) => {
        if (parent[x] !== x) {
            return getParent(parent[x]);
        }
        
        return x;
    }
    
    let union = (a, b) => {
        parent[a] = b;
    }
    
    costs.sort((a, b) => a[2] - b[2]);
    
    let idx = 0;
    
    for (const [node1, node2, cost] of costs) {
        const [nd1Parent, nd2Parent] = [getParent(node1), getParent(node2)];
        
        if (nd1Parent !== nd2Parent) {
            union(nd1Parent, nd2Parent);
            visited.add(node1);
            visited.add(node2);
            answer += cost;    
        }
        
    }
    
    return answer;
}
