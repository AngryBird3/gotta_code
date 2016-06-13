/*
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.

Hide Company Tags Google
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (M) Longest Substring Without Repeating Characters (H) Sliding Window Maximum (H) Longest Substring with At Most K Distinct Characters
Difficulty: Hard
*/
ass Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        if (s.length() == 0) {
            return 0;
        }   

        /* Algorithm
         * keep window: left and right pointer
         * and counter - # of diff char in current
         * window. 
         * if we exceed counter > k: adjust left pointer
         * till we get count <= k 
         */
    
        //Counter for each char in string
        int counter[256];
        memset(&counter, 0, sizeof(counter));
    
        int left = 0, right = 0;
        int max_left = 0, max_right = 0, max_len = 0, diff = 0;
        int i = 0;
        while (i < s.length()) {
            //printf("--- NEXT ---\n");
            //printf("s[i]: %c, left: %d, right: %d, diff: %d, max_left: %d, max_right: %d\n", s[i], left, right, diff, max_left, max_right);
            if(counter[s[i]] == 0) {
                ++counter[s[i]];
                ++diff; //Only increameting for first time
            } else{
                // If we're here; that means in current substring char
                // this char (*s) already exists
                ++counter[s[i]];
            }   
            ++right;
            /* If we already hit our different char limit; update max_len */
            if (diff == 2 && (right - left > max_right - max_left)) {
                max_left = left;
                max_right = right;
                //printf("max_left: %c, max_right: %c\n", s[max_left], s[max_right]);
            }   

            /* Adjust window by removing some char from left end */
            else if ( diff > 2 ) { 
                //printf("->>>>>>>>>>>> DEBUG --- diff: %d\n", diff);

                while(diff > 2) {
                    if(--counter[s[left]] == 0) {
                        --diff;
                    }   
                    ++left;
                    //printf("Left: %c, diff: %d\n", s[left], diff);
                }   
                    
            }   
            i++;
        }   
        //return s.substr(max_left, max_right - max_left);
        if (diff <= 1) {
            return (right- left);
        }
        return (max_right - max_left);
    }
};
