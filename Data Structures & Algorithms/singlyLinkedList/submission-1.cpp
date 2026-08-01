class LinkedList {
    vector<int> list;
public:
    LinkedList() {}

    int get(int index) {
        if (index >= list.size()) return -1;
        return list[index];
    }

    void insertHead(int val) {
        list.insert(list.begin(), val);
    }
    
    void insertTail(int val) {
        list.push_back(val);
    }

    bool remove(int index) {
        if (index >= list.size()) return false;
        list.erase(list.begin() + index);
        return true;
    }

    vector<int> getValues() {
        return list;
    }
};
