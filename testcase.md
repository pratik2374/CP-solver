

| Sample Input | Sample Output (Brute Force) | Sample Output (Optimized) |
|---------------|----------------------------|--------------------------|
| [2, 0, 2, 1, 1, 0] | [0, 0, 1, 1, 2, 2] | [0, 0, 1, 1, 2, 2] |
| [0, 1, 2, 2, 0] | [0, 0, 1, 2, 2, 2] | [0, 0, 1, 2, 2, 2] |
| [1, 1, 1] | [1,1,1] | [1,1,1] |
| [2,2,2] | [2,2,2] | [2,2,2] |
| [0,1,0] | [0,0,1] | [0,0,1] |
| [2,1,0,1] | [0,1,1,2] | [0,1,1,2] |
| [1,0,2] | [0,1,2] | [0,1,2] |
| [0,0,0] | [0,0,0] | [0,0,0] |
| [2,0,2,1,1,0] | [0,0,1,1,2,2] | [0,0,1,1,2,2] |
| [1,2,2,1] | [1,1,2,2] | [1,1,2,2] |
| [] | [] | [] |
| [0] | [0] | [0] |
| [1] | [1] | [1] |
| [2] | [2] | [2] |

Each test case ensures that both sorting functions handle various distributions of 0s, 1s, and 2s correctly, including edge cases like all elements being the same or single-element arrays.