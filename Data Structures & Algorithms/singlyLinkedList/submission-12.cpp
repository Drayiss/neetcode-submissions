class LinkedList {
    class ListNode {
        public:
            int val_;
            ListNode *next;
            ListNode(int val) {
                val_ = val;
                next = nullptr;
            }
    };
public:
    ListNode *head;
    ListNode *tail;

    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    int get(int index) {
        if (head == nullptr) return -1;

        ListNode *currentNode = head;
        for (int i = 1; i <= index; i++) {
            if (currentNode->next == nullptr) return -1;
            currentNode = currentNode->next;
        }
        return currentNode->val_;
    }

    void insertHead(int val) {
        ListNode *newNode = new ListNode(val);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        }
        else {
            newNode->next = head;
            head = newNode;
        }
    }
    
    void insertTail(int val) {
        ListNode *newNode = new ListNode(val);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    bool remove(int index) {
        if (head == nullptr || index < 0) return false;
    
        if (head == tail) {
            if (index == 0) {
                delete head;
                head = nullptr;
                tail = nullptr;
                return true;
            }
            return false;
        }
    
        if (index == 0) {
            ListNode* removalNode = head;
            head = head->next;
            delete removalNode;
            return true;
        }

        ListNode *prevNode = head;
        for (int i = 1; i < index; i++) {
            prevNode = prevNode->next;
            if (prevNode->next == nullptr) {
                return false;
            }
        }
        
        ListNode *removalNode = prevNode->next;
        if (removalNode->next == nullptr) {
            delete removalNode;
            prevNode->next = nullptr;
            tail = prevNode;
            return true;
        }
        prevNode->next = removalNode->next;
        delete removalNode;
        return true;
        
    }

    vector<int> getValues() {
        vector<int> allVals;
        ListNode *currentNode = head;
        while (currentNode != nullptr) {
            allVals.push_back(currentNode->val_);
            currentNode = currentNode->next;
        }
        return allVals;
    }
};
