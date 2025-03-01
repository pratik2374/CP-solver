#include <stdio.h>
#include <stdlib.h>

void brute_force_sort(int* nums, int numsSize) {
    int count0 = 0, count1 = 0, count2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) count0++;
        else if (nums[i] == 1) count1++;
        else count2++;
    }
    int index = 0;
    while (count0-- > 0) nums[index++] = 0;
    while (count1-- > 0) nums[index++] = 1;
    while (count2-- > 0) nums[index++] = 2;
}

void optimized_sort(int* nums, int numsSize) {
    int low = 0, high = numsSize - 1, current = 0;
    while (current <= high) {
        if (nums[current] == 0) {
            int temp = nums[low];
            nums[low] = nums[current];
            nums[current] = temp;
            low++;
        } else if (nums[current] == 2) {
            int temp = nums[high];
            nums[high] = nums[current];
            nums[current] = temp;
            high--;
        }
        current++;
    }
}

int main() {
    int nums[] = {2, 0, 2, 1, 1, 0};
    int size = sizeof(nums) / sizeof(nums[0]);
    
    int* brute_force = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) brute_force[i] = nums[i];
    brute_force_sort(brute_force, size);
    
    int* optimized = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) optimized[i] = nums[i];
    optimized_sort(optimized, size);
    
    printf("Brute Force Result: ");
    for (int i = 0; i < size; i++) printf("%d ", brute_force[i]);
    printf("\n");
    
    printf("Optimized Result: ");
    for (int i = 0; i < size; i++) printf("%d ", optimized[i]);
    printf("\n");
    
    free(brute_force);
    free(optimized);
    return 0;
}