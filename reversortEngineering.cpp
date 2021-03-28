#include <iostream>
#include <cstdlib>
using namespace std;

int calCost(int n, int *reversePoints, int end) {
    int cost = 0;
    for (int i = 0; i < n - 1 && i <= end; i++) {
        if (reversePoints[i] == 1) {
            cost += i + 2;
        } else {
            cost += 1;
        }
    }
    return cost;
}

void copyReversePoint(int n, int *src, int *target) {
    for (int i = 0; i < n; i++) {
        target[i] = src[i];
    }
}

int calMaxCost(int start, int end) {
    int cost = 0;
    for (int i = start; i < end; i++) {
        cost += i;
    }
    return cost;
}

void initReversePoints(int *reversePoints, int n) {
    for (int i = 0; i < n - 1; i++) {
        reversePoints[i] = -1;
    }
}

void printReversePoints(int* reversePoints, int size) {
    for (int i = 0; i < size; i++) {
        cout << reversePoints[i] << " ";
    }
    cout << endl;
}

int* findReversePoint(int n, int c, int* reversePoints, bool *found,
    int currentIndex) {
    if (*found) {
        return 0;
    }
    if (currentIndex >= n - 1) {
        if (calCost(n, reversePoints, currentIndex-1) == c) {
            *found = true;
            return reversePoints;
        } else {
            return 0;
        }
    }
    if ((calCost(n, reversePoints, currentIndex-1) + calMaxCost(currentIndex+1, n+1) < c)
        || calCost(n, reversePoints, currentIndex-1) >= c) {
        return 0;
    }

    if (reversePoints == 0) {
        reversePoints = (int *)malloc(sizeof(int) * (n-1));
        initReversePoints(reversePoints, n);
    }


    int *reversePointsA = (int *)malloc(sizeof(int) * (n-1));
    copyReversePoint(n-1, reversePoints, reversePointsA);
    reversePointsA[currentIndex] = 1;
    int *resultA = findReversePoint(n, c, reversePointsA, found, currentIndex+1);

    int *reversePointsB = (int *)malloc(sizeof(int) * (n-1));
    copyReversePoint(n-1, reversePoints, reversePointsB);
    reversePointsB[currentIndex] = 0;
    int *resultB = findReversePoint(n, c, reversePointsB, found, currentIndex+1);

    return resultA != 0 ? resultA : resultB;
}

void reverse(int *arr, int start, int end) {
    int size = end - start;
    int tmp[size];
    for (int i = 0; i < size; i++) {
        tmp[size-i-1] = arr[start+i];
    }
    for (int i = 0; i < size; i++) {
        arr[start+i] = tmp[i];
    }
}

void generateReverseArray(int *arr, int n, int *reversePoints) {
    for (int i = 0; i < n-1; i++) {
        if (reversePoints[i]) {
            reverse(arr, n - i - 2, n);
        }
    }
}

void initReverseArray(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }
}

void printResult(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << ((i < n - 1) ? " " : "");
    }
    cout << endl;
}

int main() {
    int t, n, c;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> c;
        bool found = false;
        int *reversePoints = findReversePoint(n, c, 0, &found, 0);
        cout << "Case #" << i << ": ";
        if (reversePoints != 0) {
            int reverseArray[n];
            initReverseArray(reverseArray, n);
            generateReverseArray(reverseArray, n, reversePoints);
            printResult(reverseArray, n);
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}