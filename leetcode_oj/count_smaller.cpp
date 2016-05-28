class Solution {
public:

void help(vector<int>& nums, vector<int>& vec, vector<int>& copy, int l, int r, int smaller[]) {

    if(l==r) return;

    int m = l+(r-l)/2;
    help(nums, vec, copy, l, m, smaller);
    help(nums, vec, copy, m+1, r, smaller);

    int i=l, j=m+1, k=l;
    while(i<=m || j<=r) {
        if( j==r+1 || (i<=m &&  nums[vec[i]] <= nums[vec[j]])) {
            copy[k++] = vec[i];
            smaller[vec[i]] += j-m-1;
            i++;
        }
        else copy[k++] = vec[j++];
    }

    for(int i=l; i<=r; i++) {
        vec[i] = copy[i];
    }
}

vector<int> countSmaller(vector<int>& nums) {
    vector<int> res;
    if(nums.empty()) return res;

    vector<int> vec, copy;
    for(int i=0; i<nums.size(); i++) {
        vec.push_back(i);
        copy.push_back(i);
    }


    int smaller[nums.size()];
    for(int i=0; i<nums.size(); i++) {
        smaller[i] = 0;
    }


    help(nums, vec, copy, 0, vec.size()-1, smaller);


    for(int i: smaller) {
        res.push_back(i);
    }

    return res;
}

};
