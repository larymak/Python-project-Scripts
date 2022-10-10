//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n,t;
    cin>>n>>t;
    string a;
    cin>>a;
    while(t--){
        for(int i=0;i<n-1;i++)
        if(a[i]=='B' && a[i+1]=='G') {
            swap(a[i],a[i+1]);
            i++;
        }
    }
    cout<<a<<endl;
    return 0;
}