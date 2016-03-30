/*
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?

Show Company Tags
Show Tags
Hide Similar Problems
*/

class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
		/* Algorithm:
		 * Keep track of minimum cost with two colors (i.e. index - 0..k)
		 * if current index is same as last1 go with previous house color last2
		 * that way we always pick minimum
		 * 
		 * Why we have another set of index of minimum cost (min and last)
		 * For ith house we're computing what would be minimum cost
		 * assuming till my [i-1] house it was last1 index and last2 index
		 * which had minimum cost1 and minimum cost2
		 * For next (i+1) we can keep track new min1, min2
		 *
		 * we cant change in middle last1, last2 otherwise two house
		 * might end up having same color!!
		 *
		 * opt[i][j] = cost[i][j] + j != min1 ? opt[i-1][min1] : opt[i-1][min2]
		 *
		 * In english: return opt[n][min1] : minimum cost to paint till nth houses
		 */
		int n = costs.size();
		if (n == 0) return 0;
		int i, j, k = costs[0].size();
		int last1 = -1, last2 = -1, min1 = -1, min2 = -1;
		for (i = 0; i < n; i++) {
			last1 = min1; last2 = min2;
			for (j = 0; j < k; j++) {
				if (j == last1) {
					costs[i][j] += last2 < 0 ? 0 : costs[i-1][last2];
				} else {
					costs[i][j] += last1 < 0 ? 0 : costs[i-1][last1];
				}

				//Update min1 and min2 for next(i+1)th computation
				if (min1 < 0 || costs[i][j] < costs[i][min1]) {
					min1 = j;
					min2 = min1;
				} else if (min2 < 0 || costs[i][j] < costs[i][min2]) {
					min2 = j;
				}
			}
		}
		return costs[n-1][min1];
    }
};
