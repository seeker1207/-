function Node(name) {
    this.name = name;
    this.exist = 'O';
    this.next = null;
    this.prev = null;
}

function LinkedList() {
    this.head = null;
    this.tail = null;
    this.nowNode = null;
    this.cache = [];
    
    this.append = (name) => {
        if (this.head === null) {
            this.head = new Node(name);
            this.tail = this.head;
            return;
        }
        let newNode = new Node(name);
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
    }
    
    this.search = (idx) => {
        let nowIdx = 0;
        this.nowNode = this.head;
        while (idx > nowIdx) {
            this.nowNode = this.nowNode.next;
            nowIdx++;
        }
    }
    
    this.moveUp = (moveCnt) => {
        let cnt = 0;
        while (cnt < moveCnt) {
            this.nowNode = this.nowNode.prev;
            if (this.nowNode.exist == 'O') cnt++;
        }
    }
    
    this.moveDown = (moveCnt) => {
        let cnt = 0;
        while (cnt < moveCnt) {
            this.nowNode = this.nowNode.next;
            if (this.nowNode.exist == 'O') cnt++;
        }
    }
    
    this.delete = () => {
        this.nowNode.exist = 'X';
        this.cache.push(this.nowNode);
        
        if (this.nowNode !== this.tail) {
            this.nowNode = this.nowNode.next;
        } else {
            this.nowNode = this.tail.prev;
        }
    }
    
    this.recover = () => {
        this.cache[this.cache.length-1].exist = 'O';
        this.cache.pop();
    }
}

function solution(n, k, cmd) {
    var answer = '';
    let linkedList = new LinkedList();
    
    for (let i=0; i<n; i++) {
        linkedList.append(i);
    }
    
    linkedList.search(k);
    
    for (let cmdElm of cmd) {
        const [cmdType, cnt] = cmdElm.split(' ');
        const cntInt = parseInt(cnt);
        switch(cmdType) {
            case 'D':
                linkedList.moveDown(cntInt);
                break;
            case 'U':
                linkedList.moveUp(cntInt);
                break;
            case 'C':
                linkedList.delete();
                break;
            case 'Z':
                linkedList.recover();
                break;
        }
    }
    
    let node = linkedList.head;

    while (node) {
        answer += node.exist;
        node = node.next;
    }
    return answer;
}
