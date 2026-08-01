class DynamicArray {
    int* myArray;
    int length;
    int capacity;
public:

    DynamicArray(int capacity) : capacity(capacity), length(0) {
        myArray = new int[capacity];
    }

    int get(int i) {
        return myArray[i];
    }

    void set(int i, int n) {
        myArray[i] = n;
    }

    void pushback(int n) {
        if (length == capacity) {
            resize();
        }
        myArray[length] = n;
        length++;
    }

    int popback() {
        if (length > 0) {
            length--;
        }
        return myArray[length];
    }

    void resize() {
        capacity *= 2;
        auto newArray = new int[capacity];
        for (auto i = 0; i < length; i++) {
            newArray[i] = myArray[i];
        }
        delete[] myArray;
        myArray = newArray;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
