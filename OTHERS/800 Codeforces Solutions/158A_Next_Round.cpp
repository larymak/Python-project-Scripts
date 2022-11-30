//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    vector<int> a;
    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        a.push_back(temp);
    }
    int c=a[k-1];
    int count=0;
    for(int x:a){
        if(x>=c && x>0) count++;
    }
    cout<<count<<endl;
    return 0;
}