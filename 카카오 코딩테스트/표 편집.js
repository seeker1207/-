function Node(name) {
    this.name = name;
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
            cnt++;
        }
    }
    
    this.moveDown = (moveCnt) => {
        let cnt = 0;
        while (cnt < moveCnt) {
            this.nowNode = this.nowNode.next;
            cnt++;
        }
    }
    
    this.delete = () => {
        const temp = this.nowNode;
        this.cache.push([temp, this.nowNode.prev, this.nowNode.next]);
        
        if (this.nowNode === this.head) {
            this.head = this.nowNode.next;
            this.nowNode.next.prev = null;
            this.nowNode = this.nowNode.next;
        } else if (this.nowNode === this.tail) {
            this.tail = this.nowNode.prev;
            this.nowNode.prev.next = null;
            this.nowNode = this.nowNode.prev;
        } else {
            this.nowNode.prev.next = this.nowNode.next;
            this.nowNode.next.prev = this.nowNode.prev;
            this.nowNode = this.nowNode.next;
        }
    }
    
    this.recover = () => {
        let [target, prev, next] = this.cache.pop();
        
        if (prev) prev.next = target;
        if (next) next.prev = target;
        if (next === this.head) this.head = target;
        if (prev === this.tail) this.tail = target;
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

    for (let i=0; i<n; i++) {
        if (node === null) {
                answer += 'X';
                continue;
        }
        if (i === +node.name) {
            answer += 'O';
            // console.log(node);
            node = node.next;
        } else {
            answer += 'X';
        }
    }

    return answer;
}
