#include <vector>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <deque>

using namespace std;
class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int>> ans;
        if(matrix.empty() || matrix[0].empty()) return ans;
        int r = matrix.size(), c = matrix[0].size();
        vector<vector<int>>pac(r, vector<int>(c,0));
        auto atl = pac;
        deque<pair<int,int>>aq,pq;

        for(int i = 0; i < r; i++)
        {
            atl[i][c-1] = pac[i][0] = 1;
            aq.push_back(make_pair(i,c-1));
            pq.push_back(make_pair(i,0));
        }

        for(int i = 0; i < c; i++)
        {
            atl[r-1][i] = pac[0][i] = 1;
            aq.push_back(make_pair(r-1,i));
            pq.push_back(make_pair(0,i));
        }

        while(!aq.empty())
        {
            int m = aq.front().first;
            int n = aq.front().second;
            int debug = 0;
            aq.pop_front();
            if(m>0 && atl[m-1][n] == 0 && matrix[m-1][n]>=matrix[m][n])
            {
                atl[m-1][n] = 1;
                aq.push_back(make_pair(m-1,n));
            }

            if(n>0 && atl[m][n-1] == 0 && matrix[m][n-1]>=matrix[m][n])
            {
                atl[m][n-1] = 1;
                aq.push_back(make_pair(m,n-1));
            }

            if(m+1 < r && atl[m+1][n] == 0 && matrix[m+1][n]>=matrix[m][n])
            {
                atl[m+1][n] = 1;
                aq.push_back(make_pair(m+1,n));
            }

            if(n+1 < c && atl[m][n+1] == 0 && matrix[m][n+1]>=matrix[m][n])
            {
                atl[m][n+1] = 1;
                aq.push_back(make_pair(m,n+1));
            }
            debug = 0;
        }


        while(!pq.empty())
        {
            int m = pq.front().first;
            int n = pq.front().second;
            pq.pop_front();
            if(m>0 && pac[m-1][n] == 0 && matrix[m-1][n]>=matrix[m][n])
            {
                pac[m-1][n] = 1;
                pq.push_back(make_pair(m-1,n));
            }

            if(n>0 && pac[m][n-1] == 0 && matrix[m][n-1]>=matrix[m][n])
            {
                pac[m][n-1] = 1;
                pq.push_back(make_pair(m,n-1));
            }

            if(m+1 < r && pac[m+1][n] == 0 && matrix[m+1][n]>=matrix[m][n])
            {
                pac[m+1][n] = 1;
                pq.push_back(make_pair(m+1,n));
            }

            if(n+1 < c && pac[m][n+1] == 0 && matrix[m][n+1]>=matrix[m][n])
            {
                pac[m][n+1] = 1;
                pq.push_back(make_pair(m,n+1));
            }
        }

        cout << " Visited pacific " << endl;

        for (const auto& inner : pac) {
            for (const auto& item : inner) {
                  cout << item << " ";
            }
            cout << endl;
        }

        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                if(atl[i][j] && pac[i][j]) ans.push_back(make_pair(i,j));

        return ans;
    }
};

int main() {
  Solution sol;
  std::vector<std::vector<int> > matrix(5, std::vector<int>(5));
  matrix[0] = {1,2,2,3,5};
  matrix[1] = {3,2,3,4,4};
  matrix[2] = {2,4,5,3,1};
  matrix[3] = {6,7,1,4,5};
  matrix[4] = {5,1,1,2,4};

  vector<pair<int, int>> common = sol.pacificAtlantic(matrix);
  return 0;
}
