/*
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
*/

class Solution {
public:
    int bulbSwitch(int n) {
    	/*
		 * For bulb b, it will get toggled during the rounds
		 * of its factors:
		 * e.g. bulb 6 will be toggled at 1, 2, 3, 6 and so on
		 * and bulb 4 will be toggled at 1, 2, 4 
		 * If bulb toggles odd # of times, its gonna be ON at the
		 * end, otherwise not.
		 * Now, how to find which # has odd number of factors?
		 * Perfect squares!
		 * http://mathforum.org/library/drmath/view/72126.html 
		 * Number of perfect squares: sqrt(n)
		 * http://stackoverflow.com/questions/8934919/perfect-squares-between-two-numbers
		 * If you want to find WHICH bulbs are they:
		 * from a to b
		 * (n+1)^2 = n^2 + 2n + 1
		 * to find between n^2 to (n+1)^ ...add 2n+1
		 */
		return floor(sqrt(n));
    }
};
