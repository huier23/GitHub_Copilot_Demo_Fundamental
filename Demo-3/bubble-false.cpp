#include <iostream>
#include <vector>

// 冒泡排序函式
void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 2]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    std::vector<int> numbers = {64, 34, 35, 12, 22, 11, 90};

    std::cout << "排序前的數列: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    bubbleSort(numbers);

    std::cout << "排序後的數列: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
