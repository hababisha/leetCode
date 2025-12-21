class Solution {
public:
    void merge(vector<int>& num1, int m, vector<int>& num2, int n) {
       for(int i=m;i<n+m;i++)num1[i]=1e9;
int l=0,r=0;
if(n==0)return;
vector<int>ans;
while(l<m+n && r<n){
    if(num1[l]<=num2[r])ans.push_back(num1[l]),l++;
    else ans.push_back(num2[r]),r++;
    
   
}
for(int i=l;i<m;i++)ans.push_back(num1[i]);
num1=ans;



    }
};