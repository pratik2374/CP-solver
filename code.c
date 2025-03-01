#include <stdio.h>

void brute_force(int* nums, int numsSize) {
    int count0 = 0, count1 = 0, count2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) count0++;
        else if (nums[i] == 1) count1++;
        else count2++;
    }
    for (int i = 0; i < count0; i++) nums[i] = 0;
    for (int i = count0; i < count0 + count1; i++) nums[i] = 1;
    for (int i = count0 + count1; i < numsSize; i++) nums[i] = 2;
}

void optimized(int* nums, int numsSize) {
    int low = 0, mid = 0, high = numsSize - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            int temp = nums[low];
            nums[low] = nums[mid];
            nums[mid] = temp;
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            int temp = nums[mid];
            nums[mid] = nums[high];
            nums[high] = temp;
            high--;
        }
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int nums[n];
    printf("Enter the elements (0, 1, 2): ");
    for (int i = 0; i < n; i++) scanf("%d", &nums[i]);
    
    int nums_brute[n];
    for (int i = 0; i < n; i++) nums_brute[i] = nums[i];
    brute_force(nums_brute, n);
    printf("Brute Force Sorted Array: ");
    for (int i = 0; i < n; i++) printf("%d ", nums_brute[i]);
    printf("\n");
    
    int nums_optimized[n];
    for (int i = 0; i < n; i++) nums_optimized[i] = nums[i];
    optimized(nums_optimized, n);
    printf("Optimized Sorted Array: ");
    for (int i = 0; i < n; i++) printf("%d ", nums_optimized[i]);
    printf("\n");
    
    return 0;
}