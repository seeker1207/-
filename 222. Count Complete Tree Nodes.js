/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

/*
    전체 트리의 높이는 왼쪽으로만 노드를 탐색하면 구할수 있다.
    노드가 만약 하나만 존재하면 높이는 0이다.
    노드가 하나도 없다면 높이는 -1을 반환한다.

    루트노드를 기준으로
    오른쪽의 서브트리의 높이가 전체 트리의 높이보다 하나 작은지 확인한다. 
    (왼쪽 트리와 오른쪽 트리의 높이가 같은지 확인한다.)

    만약 그렇다면, 트리의 마지막 단계의 마지막 노드는 오른쪽 서브트리에 있다. 
    따라서 높이 h-1만큼의 왼쪽 서브트리는 모두 다 차있는 완전한 트리노드이므로 
    왼쪽 서브트리의 노드 갯수인 (2^h -1)만큼의 노드 갯수를 더해주고, 
    거기에 루트노드 1개와 오른쪽 서브트리의 노드 갯수를 구하는 재귀함수를 호출한다.

    만약 아니라면, 트리의 마지막 노드는 왼쪽 서브트리에 있다는 얘기이다.
    따라서 높이 h-2 만큼의 오른쪽 서브트리는 모두 다 차있는 완전한 트리노드이다.
    오른쪽 서브트리의 노드 갯수인 (2^(h-1) - 1)만큼의 노드갯수를 더해주고,
    루트 노드 1개와 왼쪽 서브트리의 노드 갯수를 재귀함수를 통해 구해준다.
*/
var countNodes = function(root) {
    
    let getHeight = (root) => {
        if (!root) return -1;
        
        return getHeight(root.left) + 1;
    }
    
    let [nodeCnt, h] = [0, getHeight(root)];
    
    while (root) {
        if (getHeight(root.right) === h - 1) {
            nodeCnt += 1 << h;
            root = root.right;
        } else {
            nodeCnt += 1 << h - 1;
            root = root.left;
        }
        h--;
    }
    
    return nodeCnt;
};
